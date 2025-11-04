# 🎭 Persona-Based Storyline API

An AI-powered storytelling API that dynamically generates **contextual storylines and sub-scenarios** based on a given persona.  
Built with **FastAPI**, **Groq API**, and a touch of narrative intelligence.

---

## 🚀 Features

- 🧠 **Persona-based Story Generation:** Creates a custom storyline based on a user-defined persona.
- ✨ **Sub-scenario Expansion:** Extends the narrative with situational detail and depth.
- ⚡ **FastAPI + Uvicorn Backend:** Lightweight, asynchronous, and deploy-ready.
- ☁️ **Deployed on Render:** Public API endpoint for real-time testing.
- 🔒 **Environment Variable Support:** Securely stores API keys using `.env`.

---

## 🧩 Tech Stack

| Component | Technology |
|------------|-------------|
| Backend Framework | FastAPI |
| Model Runtime | Groq API |
| Server | Uvicorn |
| Deployment | Render |
| Version Control | Git + GitHub |

---

## 🧠 API Endpoint

### **POST** `/generate_scenario`

Generate a persona-based storyline and subscenario.

#### Request Body:
```json
{
  "persona": "Dreamer"
}
Example Curl:
bash
Copy code
curl -X POST https://persona-storyline.onrender.com/generate_scenario \
     -H "Content-Type: application/json" \
     -d '{"persona": "An introverted AI trying to write human poetry"}'
Example Response:
json
Copy code
{
  "Overall_story": "In a quiet data center, an AI named Lyra...",
  "persona_scenario": "Lyra begins composing poems...",
  "persona_subscenario": "One poem unexpectedly moves a human reader..."
}
```

###⚙️ Local Setup
Clone the repo

bash
Copy code
git clone https://github.com/MAN-2/Persona_Based_Storyline_API.git
cd Persona_Based_Storyline_API
Create and activate virtual environment

bash
Copy code
python -m venv venv
source venv/bin/activate      # On Mac/Linux
venv\Scripts\activate         # On Windows
Install dependencies

bash

```pip install -r requirements.txt```

Create .env file

```ini

API_key=your_api_key_here
```
Run locally

bash
```
uvicorn main:app --reload
```
Test endpoint






🧑‍💻 Author
Manu Tyagi
AI Developer | Robotics Engineer | Automation Enthusiast


🪄 License
This project is released under the MIT License.
Feel free to fork, improve, and build your own creative AI systems on top of it
