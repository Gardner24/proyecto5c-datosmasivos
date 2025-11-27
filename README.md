readme: |
  # Proyecto 5C – Big Data (Yellow Taxi NYC)

  Análisis comparativo de propinas ("tips") de los Yellow Taxis de Nueva York utilizando una arquitectura moderna basada en AWS S3, AWS Lambda, Supabase y Jupyter Notebook.

  Este proyecto es parte del curso de Datos Masivos y su objetivo es construir un flujo real de procesamiento de datos, aplicar técnicas de análisis y generar insights basados en datasets auténticos.

  ---

  # 🚀 Arquitectura General del Proyecto

  Dataset (CSV)
        → AWS S3 (Raw Layer)
              → AWS Lambda (Procesamiento)
                    → Supabase (PostgreSQL)
                          → Jupyter Notebook (Análisis & Visualización)

  ## Servicios utilizados

  | Servicio        | Función en el proyecto |
  |-----------------|-------------------------|
  | **AWS S3**      | Almacenamiento de datos crudos (datasets 2016). |
  | **AWS Lambda**  | Procesamiento automático cuando se suben archivos a S3. |
  | **Supabase**    | Base de datos PostgreSQL + API REST. |
  | **Jupyter**     | Exploración, análisis y visualización. |

  ---

  # 📁 Estructura del Repositorio

  proyecto5c-datosmasivos/
  │
  ├── docs/                       # Documentación del proyecto
  │   ├── informe_proyecto.md
  │   └── diagramas_arquitectura.png
  │
  ├── infra/                      # Infraestructura / Backend
  │   └── lambda_processors/
  │       ├── handler.py
  │       └── requirements.txt
  │
  ├── notebooks/                  # Jupyter notebooks del análisis
  │   ├── .gitkeep
  │   └── exploracion_inicial.ipynb
  │
  ├── .env.example                # Plantilla del archivo .env (segura)
  ├── .gitignore                  # Evita subir archivos sensibles
  │
  └── README.md

  ---

  # 👥 Colaboración entre Miembros del Equipo

  Este proyecto permite trabajo en equipo de manera segura.

  ## Cada miembro tendrá:
  - Su propio **usuario IAM** en AWS.
  - Su propio **Access Key & Secret Key**.
  - Acceso al repositorio como colaborador.
  - La misma URL y anon key de Supabase.

  ## Ningún miembro debe compartir:
  - Access Keys de AWS  
  - Secret Keys de AWS  
  - `service_role key` de Supabase  
  - Su archivo `.env` real  

  ---

  # ⚙️ Instalación y Configuración del Entorno

  A continuación se detallan los pasos que cada miembro del equipo debe seguir:

  ## 1️⃣ Clonar el repositorio


---

# ⚙️ Instalación y Configuración del Entorno (Guía para el Equipo)

## 1️⃣ Clonar el repositorio

bash
git clone https://github.com/Gardner24/proyecto5c-datosmasivos.git
cd proyecto5c-datosmasivos
3️⃣ Configurar el archivo .env

Copiar la plantilla:

copy .env.example .env


Editar:

notepad .env


Agregar valores:

AWS_ACCESS_KEY_ID=TU_KEY_PERSONAL
AWS_SECRET_ACCESS_KEY=TU_SECRET_PERSONAL
AWS_REGION=us-east-1

SUPABASE_URL=https://TU_PROYECTO.supabase.co
SUPABASE_KEY=TU_ANON_KEY


⚠️ El archivo .env nunca se sube a GitHub.
Está protegido por .gitignore. Cada miembro tiene su propio archivo local.

🧪 Verificación del Entorno

4️⃣ Probar carga del .env (seguro para screenshot)
from dotenv import load_dotenv
import os

load_dotenv()

print("AWS_ACCESS_KEY_ID:", os.getenv("AWS_ACCESS_KEY_ID")[:4] + "****")
print("SUPABASE_URL:", os.getenv("SUPABASE_URL"))
print("SUPABASE_KEY:", os.getenv("SUPABASE_KEY")[:6] + "****")

5️⃣ Probar conexión a AWS S3
import boto3

s3 = boto3.client("s3")
resp = s3.list_buckets()

print("Conexión S3 OK")
print("Buckets:")
for b in resp["Buckets"]:
    print(" -", b["Name"])

    from supabase import create_client
import os

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)

print("Conexión Supabase OK:", supabase is not None)


