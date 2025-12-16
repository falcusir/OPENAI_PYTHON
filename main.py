import os
from dotenv import load_dotenv
from openai import OpenAI

# 1️⃣ Cargar variables de entorno
load_dotenv()
# 2️⃣ Crear cliente de OpenAI
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    organization=os.getenv("OPENAI_ORG_ID")
)
# 3️⃣ Función para enviar un prompt a OpenAI
def consultar_openai():
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "Explícame qué es la inteligencia artificial en 3 líneas"}
            ],
            max_tokens=150,
            temperature=0.7
        )

        # 4️⃣ Mostrar respuesta
        print("Respuesta de OpenAI:\n")
        print(response.choices[0].message.content)

    except Exception as error:
        print("Error al consultar OpenAI:", error)

# 5️⃣ Ejecutar función
consultar_openai()
