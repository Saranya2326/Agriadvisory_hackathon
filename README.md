# Multilingual Agritech & Resource Advisory Assistant

A student-built web application prototype that helps farmers access agricultural information in Tamil, English and Hindi through text and browser voice features.

## Features
- Farmer profile registration (name, state, district, preferred language)
- Multilingual dashboard and advisory interface
- Rule-based starter crop advisory (not a diagnosis or guaranteed recommendation)
- Weather and mandi-price endpoints with clearly labelled demo data until official API credentials/data feeds are configured
- Soil information form and basic interpretation
- Browser speech recognition and text-to-speech where supported
- SQLite storage for farmer profiles and feedback

## Tech stack
- Frontend: React + Vite + CSS
- Backend: Python + Flask + SQLite
- Voice: Web Speech API (browser support varies)
- Integrations: API-ready service modules for weather and mandi data

## Run locally

### Requirements
- Python 3.10+
- Node.js 18+
- npm

### 1. Start backend
```bash
cd backend
python -m venv .venv
# Windows PowerShell:
.venv\\Scripts\\Activate.ps1
# macOS/Linux:
# source .venv/bin/activate
pip install -r requirements.txt
copy .env.example .env
python app.py
```
Backend runs at `http://127.0.0.1:5000`.

### 2. Start frontend (new terminal)
```bash
cd frontend
npm install
npm run dev
```
Open the Vite URL shown in the terminal (usually `http://localhost:5173`).

## Environment variables
See `backend/.env.example`. The starter app runs without external API keys. In that mode, weather and mandi results are **demo/sample data**, not live official data. Do not present sample values as current real-world data.

## API routes
- `GET /api/health`
- `POST /api/farmers`
- `GET /api/farmers/<id>`
- `POST /api/advisory`
- `GET /api/weather?district=...`
- `GET /api/mandi?commodity=...&district=...`
- `POST /api/soil-advice`
- `POST /api/feedback`

## Important data and safety notes
- The advisory engine is a transparent rule-based prototype. It does not train an AI model.
- The optional AI/RAG component is not connected in this starter version. Add it only after selecting a model provider, approved agricultural knowledge sources, and an evaluation process.
- Weather/market integrations need valid data-provider access and must be tested. Always display source and last-updated time.
- Soil and crop suggestions are general information. Farmers should confirm high-impact decisions with a local agriculture officer/KVK, especially pesticide, fertilizer and disease-treatment decisions.
- Never enter secrets into source code or commit `.env`.

## Project structure
```text
agritech-assistant/
├── backend/
│   ├── app.py
│   ├── database.py
│   ├── advisory.py
│   ├── services/
│   │   ├── weather_service.py
│   │   └── mandi_service.py
│   ├── requirements.txt
│   └── .env.example
└── frontend/
    ├── index.html
    ├── package.json
    ├── vite.config.js
    └── src/
        ├── main.jsx
        ├── App.jsx
        └── style.css
```
