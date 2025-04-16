import streamlit as st
import requests

# ----------------- CONFIGURACIÓN -------------------
API_KEY = st.secrets["API_KEY"]  # Asegurate de tenerlo en .streamlit/secrets.toml
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro-latest:generateContent"

# ----------------- INTERFAZ -------------------
breeds = [
    {"name": "Australian Shepherd", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Australian_Shepherd_blue_merle_standing.jpg/440px-Australian_Shepherd_blue_merle_standing.jpg"},
    {"name": "Basset Hound", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Basset_Hound_standing.jpg/440px-Basset_Hound_standing.jpg"},
    {"name": "Beagle", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Beagle_400.jpg/440px-Beagle_400.jpg"},
    {"name": "Bloodhound", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Bluthund.jpg/440px-Bluthund.jpg"},
    {"name": "Border Collie", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Border_collie_laying_down_in_the_grass.jpg/440px-Border_collie_laying_down_in_the_grass.jpg"},
    {"name": "Boxer", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Boxer_dog.jpg/440px-Boxer_dog.jpg"},
    {"name": "Chihuahua", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Chihuahua_longcoat_white.JPG/440px-Chihuahua_longcoat_white.JPG"},
    {"name": "Cocker Spaniel", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/English_Cocker_Spaniel_standing_on_log.jpg/440px-English_Cocker_Spaniel_standing_on_log.jpg"},
    {"name": "Corgi", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Pembroke_Welsh_Corgi_600.jpg/440px-Pembroke_Welsh_Corgi_600.jpg"},
    {"name": "Dachshund", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Black_and_Tan_Dachshund_standing.jpg/440px-Black_and_Tan_Dachshund_standing.jpg"},
    {"name": "Doberman Pinscher", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Dobermann_sitting.JPG/440px-Dobermann_sitting.JPG"},
    {"name": "French Bulldog", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/French_bulldog.JPG/440px-French_bulldog.JPG"},
    {"name": "German Shepherd", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/German_Shepherd_Dog.jpg/440px-German_Shepherd_Dog.jpg"},
    {"name": "Golden Retriever", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Golden_Retriever_Carlos.jpg/440px-Golden_Retriever_Carlos.jpg"},
    {"name": "Great Dane", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Great_Dane_standing_in_white_background.jpg/440px-Great_Dane_standing_in_white_background.jpg"},
    {"name": "Labrador Retriever", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Labrador_on_Quantock_%282175262184%29.jpg/440px-Labrador_on_Quantock_%282175262184%29.jpg"},
    {"name": "no raza", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/Collage_of_Unknown_Dog_Breeds.jpg/440px-Collage_of_Unknown_Dog_Breeds.jpg"},
    {"name": "Pitbull", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Pit_bull_in_grass.jpg/440px-Pit_bull_in_grass.jpg"},
    {"name": "Poodle", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Full_attention_%28809205187%29.jpg/440px-Full_attention_%28809205187%29.jpg"},
    {"name": "Pug", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Pug_600.jpg/440px-Pug_600.jpg"},
    {"name": "Rottweiler", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Rottweiler_standing_profile.jpg/440px-Rottweiler_standing_profile.jpg"},
    {"name": "Shetland Sheepdog", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Sheltie_standing.jpg/440px-Sheltie_standing.jpg"},
    {"name": "Shih Tzu", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Shih_Tzu_lying_on_a_sofa.jpg/440px-Shih_Tzu_lying_on_a_sofa.jpg"},
    {"name": "Yorkshire Terrier", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Yorkshire_Terrier_Puppy.jpg/440px-Yorkshire_Terrier_Puppy.jpg"}
]
age_ranges = ["0-3 meses", "3-6 meses", "6-9 meses", "9-12 meses", "1 año - 3 años", "4-6 años", "7-9 años", "10-12 años", "13 años o más"]

st.title("🐾 Entrenador Inteligente para Mascotas")

raza_name = st.selectbox("Seleccione la raza", [breed["name"] for breed in breeds])
raza = next(breed for breed in breeds if breed["name"] == raza_name)

st.image(raza["image"], width=200)

edad = st.selectbox("Seleccione la edad", age_ranges)
problema = st.text_area("Describa el problema a solucionar de su mascota")
personalidad = st.multiselect("Seleccione la personalidad", ["Amigable", "Juguetón", "Cauteloso", "Energético", "Relajado"])
personalidad_extra = st.text_area("Agregar extra información sobre la personalidad")
usuario_rutina = st.text_area("Tu rutina diaria")
familia_rutina = st.text_area("Rutina familiar (incluyendo la de tu mascota)")

# ----------------- BOTÓN DE ENVÍO -------------------
if st.button("Solicitar entrenamiento"):
    if not raza_name or not edad or not problema or not personalidad or not usuario_rutina or not familia_rutina:
        st.error("Por favor, complete todos los campos antes de solicitar el entrenamiento.")
    else:
        with st.spinner("Generando rutina personalizada con IA..."):

            # ----------------- PROMPT -------------------
            prompt = f"""
            Actuá como un entrenador canino profesional. Generá una rutina de entrenamiento personalizada para un perro con los siguientes datos:

        - Raza: {raza}
        - Edad: {edad}
        - Problema a corregir: {problema}
        - Personalidad: {', '.join(personalidad)} {personalidad_extra}
        - Rutina del dueño: {usuario_rutina}
        - Rutina familiar: {familia_rutina}

        El entrenamiento debe ser realista y adaptable a la vida diaria del usuario.
        """

        # ----------------- LLAMADO A GEMINI -------------------
        headers = {
            "Content-Type": "application/json"
        }

        payload = {
            "contents": [
                {
                    "parts": [{"text": prompt}]
                }
            ]
        }

        response = requests.post(
            f"{GEMINI_API_URL}?key={API_KEY}",
            headers=headers,
            json=payload
        )

        if response.status_code == 200:
            result = response.json()
            reply = result['candidates'][0]['content']['parts'][0]['text']
            st.markdown("### ✅ Rutina sugerida por Gemini:")
            st.write(reply)
        else:
            st.error("Hubo un error al conectar con la API de Gemini. Verificá tu API Key o el modelo.")
            st.code(response.text, language='json')
