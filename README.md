# Proyecto 5C – Big Data (Yellow Taxi NYC)
Análisis comparativo de propinas ("tips") de los Yellow Taxis de Nueva York usando una arquitectura moderna basada en AWS S3, AWS Lambda, Supabase y Jupyter Notebook.

Este proyecto forma parte del curso de Datos Masivos y tiene como objetivo construir un flujo de datos real, procesar datasets auténticos y generar visualizaciones y conclusiones basadas en un caso práctico.

---

# 🚀 Arquitectura General

El flujo de datos implementado en este proyecto es:

Dataset (CSV)
→ AWS S3 (Raw Layer)
→ AWS Lambda (Procesamiento automático)
→ Supabase (Base de Datos PostgreSQL)
→ Jupyter Notebook (Análisis y Visualización)


### **Servicios utilizados**

| Servicio        | Rol en el proyecto |
|-----------------|--------------------|
| **AWS S3**      | Almacena los datasets crudos (enero y febrero 2016). |
| **AWS Lambda**  | Procesa automáticamente los archivos al subirse a S3. |
| **Supabase**    | Actúa como base de datos y API REST para guardar las métricas procesadas. |
| **Jupyter**     | Herramienta principal para análisis, gráficos y conclusiones del equipo. |

---

# 📁 Estructura del Repositorio
│
├── docs/ # Documentación del proyecto
│ ├── informe_proyecto.md
│ └── diagramas_arquitectura.png
│
├── infra/ # Infraestructura y código backend
│ └── lambda_processors/ # Código para la función AWS Lambda
│ ├── handler.py
│ └── requirements.txt
│
├── notebooks/ # Jupyter notebooks del análisis
│ ├── .gitkeep
│ └── exploracion_inicial.ipynb
│
├── .env.example # Plantilla (segura) del archivo de configuración
├── .gitignore # Archivos que deben ser ignorados por Git
│
└── README.md # Este archivo


---

# 👥 Colaboración en Equipo

Todos los miembros del equipo trabajan sobre el mismo repositorio, siguiendo estas reglas:

### **Cada miembro tendrá:**
- Su propio **usuario IAM** dentro de la cuenta AWS del proyecto.
- Su propio **Access Key + Secret Key**.
- Acceso de lectura/escritura al bucket S3 asignado.
- Acceso como colaborador al repositorio de GitHub.
- La misma URL y **anon key** de Supabase.

### **Ningún miembro comparte:**
❌ Access Keys  
❌ Secret Keys  
❌ service_role key de Supabase  
❌ `.env` real  

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


