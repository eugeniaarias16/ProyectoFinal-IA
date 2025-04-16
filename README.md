¡Perfecto! Con esos datos, acá tenés el **README.md final mejorado**, adaptado a tu proyecto real con todo lo que usaste (Google Presentaciones, Gemini, Groq, CLIne, etc.):

---

# 🐶 DogTrainer AI – Asistente Inteligente para el Entrenamiento de Perros

## 📘 Documento del Proyecto Final  
📎 [Presentación en Google Slides](https://docs.google.com/presentation/d/1PdloXlRW_gGCgJ2dsw3lM4Tx4SPMGqcnyyI30aNNNic/edit?usp=sharing) *(enlace a completar)*

---

## 🎯 Descripción

**DogTrainer AI** es una **aplicación web construida con Python y Streamlit**, diseñada para generar **rutinas de entrenamiento personalizadas para perros**.  
La aplicación permite a los usuarios ingresar información sobre su mascota (raza, edad, personalidad, problemas de conducta) y su contexto (rutina del dueño y familiar). Con esos datos, se genera un **prompt dinámico** que es procesado por una **IA generativa (Gemini 2.5)** para ofrecer recomendaciones concretas y adaptadas.

El proyecto se desarrolló en el marco del curso final de IA, y la presentación fue realizada en **Google Presentaciones**.

---

## 🧠 Herramientas y Tecnologías Utilizadas

| Tipo | Herramienta / Tecnología |
|------|---------------------------|
| Lenguaje principal | Python 3.10 |
| Framework web | Streamlit |
| IDE | Visual Studio Code + Copilot |
| API IA original | Groq API (con modelo `mixtral-8x7b`) |
| API IA final | Google Gemini 2.5 |
| Asistente IA usado | CLIne |
| Presentación final | Google Presentaciones |

---

## 💡 Funcionalidades de la App

* Formulario con inputs guiados para:
  - ✅ Raza del perro
  - ✅ Edad
  - ✅ Problemas de conducta
  - ✅ Personalidad (multiselección + texto libre)
  - ✅ Rutina del dueño y familiar
* Generación dinámica del prompt con todos los datos.
* Consulta a **Gemini 2.5** mediante su API y recuperación de una respuesta entrenada.
* Visualización clara del plan de entrenamiento sugerido.
* Control de errores en conexión con la API.
* Interfaz intuitiva, lista para ejecución local o despliegue en la nube.

---

## 🛠 Instalación y Configuración

### 1. Clonación o descarga del repositorio

```bash
git clone https://github.com/tuusuario/dogtrainer-ai.git
cd dogtrainer-ai
```

### 2. Crear entorno virtual (recomendado)

```bash
python -m venv env
env\Scripts\activate   # en Windows
# source env/bin/activate   # en Linux/Mac
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar tu API Key de Gemini

1. Crear la carpeta `.streamlit` (si no existe).
2. Dentro, crear el archivo `secrets.toml` con este contenido:

```toml
API_KEY="TU_CLAVE_DE_GEMINI"
```

> Recordá generar tu clave desde [Google AI Studio](https://makersuite.google.com/app) o [console.cloud.google.com](https://console.cloud.google.com).

---

## ▶️ Cómo Ejecutar la App

```bash
streamlit run app.py
```

Esto abrirá automáticamente la app en tu navegador.

---

## 🧪 Ejemplo de Uso

1. Completá el formulario con los datos de tu mascota y tu rutina.
2. Hacé clic en **"Solicitar entrenamiento"**.
3. La IA responderá con un plan detallado de entrenamiento adaptado a tu situación.

---

## 📌 Notas Técnicas

- Inicialmente se probó el modelo **GROQ API** (mixtral), pero se cambió a **Gemini 2.5** debido a limitaciones de tokens.
- Se utilizó **CLIne** como asistente de desarrollo para generar código y probar prompts.
- El proyecto fue documentado y presentado en **Google Presentaciones**.

---
