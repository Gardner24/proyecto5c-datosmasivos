import json
import boto3
import csv
import os
import urllib.request
import codecs

s3 = boto3.client('s3')

def lambda_handler(event, context):
    print("--- INICIO DE PROCESO ---")
    
    # 1. VARIABLES DE ENTORNO
    try:
        bucket_name = os.environ['BUCKET_NAME']
        supabase_url = os.environ['SUPABASE_URL']
        supabase_key = os.environ['SUPABASE_KEY']
    except KeyError as e:
        return {'statusCode': 500, 'body': json.dumps(f"Error: Falta variable de entorno {str(e)}")}

    # 2. ARCHIVO A PROCESAR (mes 1 o 2)
    file_key = event.get('file_key', 'DataSet/yellow_tripdata_2016-01.csv')

    if "01" in file_key:
        month_label = "01-2016"
    elif "02" in file_key:
        month_label = "02-2016"
    else:
        month_label = "Unknown"

    print(f"Procesando archivo: {file_key} | Mes: {month_label}")

    try:
        # 3. LEER CSV DESDE S3 (streaming)
        obj = s3.get_object(Bucket=bucket_name, Key=file_key)
        stream = codecs.getreader('utf-8')(obj['Body'])
        csv_reader = csv.DictReader(stream)

        # Variables acumuladas
        total_tip = 0.0
        total_fare = 0.0
        count = 0
        payment_type_count = {}

        print("Sumando filas...")

        for row in csv_reader:
            try:
                tip = float(row["tip_amount"])
                fare = float(row["fare_amount"])
                payment_type = row.get("payment_type", "Unknown")

                # Contar métodos de pago
                if payment_type not in payment_type_count:
                    payment_type_count[payment_type] = 0
                payment_type_count[payment_type] += 1

                if tip >= 0 and fare >= 0:
                    total_tip += tip
                    total_fare += fare
                    count += 1

            except Exception:
                continue

        # Cálculos finales
        avg_tip = (total_tip / count) if count > 0 else 0
        avg_tip_pct = (total_tip / total_fare * 100) if total_fare > 0 else 0

        # 6. PREPARAR DATA PARA SUPABASE (incluye payment_type)
        data = {
            "month_label": month_label,
            "total_trips": count,
            "total_tip_amount": total_tip,
            "total_fare_amount": total_fare,
            "avg_tip": avg_tip,
            "avg_tip_pct": avg_tip_pct,
            "source_file": file_key,
            "median_tip": 0,
            "stddev_tip": 0,
            "payment_type_summary": payment_type_count   # <<<<<< AÑADIDO
        }

        # 7. GUARDAR EN SUPABASE
        headers = {
            "apikey": supabase_key,
            "Authorization": f"Bearer {supabase_key}",
            "Content-Type": "application/json",
            "Prefer": "return=minimal"
        }

        req = urllib.request.Request(
            f"{supabase_url}/rest/v1/monthly_tips",
            data=json.dumps(data).encode('utf-8'),
            headers=headers,
            method='POST'
        )

        with urllib.request.urlopen(req) as response:
            print(f"Guardado en Supabase con código: {response.getcode()}")

        return {
            'statusCode': 200,
            'body': json.dumps(f'ÉXITO: Mes {month_label} procesado.')
        }

    except Exception as e:
        print(f"ERROR: {str(e)}")
        raise e
