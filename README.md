🌾 Multilingual Agritech & Resource Advisory Assistant

A student-built web application prototype that helps Indian farmers access agricultural information in Tamil, English, and Hindi through a simple and user-friendly digital platform.

1. Project Overview

The Multilingual Agritech & Resource Advisory Assistant is a web-based application designed to make agricultural information more accessible to farmers across India.

The platform provides a multilingual dashboard where farmers can access crop advisory, weather information, mandi market prices, and soil-related guidance.

It aims to support farmers in accessing useful agricultural information and making informed farming decisions through technology.

2. Problem Statement

Farmers across India face several challenges when accessing agricultural information.

* Limited access to reliable agricultural information.
* Difficulty identifying suitable crops and farming practices.
* Lack of awareness about weather conditions and market prices.
* Language barriers in existing digital agricultural platforms.
* Difficulty accessing different agricultural services from a single platform.

These challenges can affect farming decisions and make it difficult for farmers to access the information they need.

3. Proposed Solution

We propose a Multilingual Agritech & Resource Advisory Assistant that brings essential agricultural information together in one platform.

The application provides:

* Multilingual support in Tamil, English, and Hindi.
* Farmer profile registration.
* Basic rule-based crop advisory.
* Weather information.
* Mandi market price information.
* Soil information and basic interpretation.
* A simple and user-friendly dashboard.
* Feedback submission facility.

The goal is to improve access to agricultural information through a centralized and easy-to-use platform.

4. Technologies Used

Frontend

* React.js
* Vite
* HTML
* CSS
* JavaScript

Backend

* Python
* Flask
* REST API

Database

* SQLite

Development Tools

* Visual Studio Code
* Git
* GitHub

External Integrations

* API-ready weather service module
* API-ready mandi price service module

5. Features

1. Multilingual Interface

Supports Tamil, English, and Hindi to make agricultural information easier to understand.

2. Farmer Registration

Allows farmers to register their name, state, district, and preferred language.

3. Crop Advisory

Provides basic crop-related suggestions using a rule-based advisory system.

4. Weather Information

Provides a dedicated section for accessing weather-related information.

5. Mandi Market Prices

Helps farmers access agricultural commodity market price information.

6. Soil Information

Allows users to enter soil-related details and receive basic soil interpretation.

7. User Dashboard

Provides a centralized dashboard to access different agricultural services.

8. Feedback System

Allows farmers to submit feedback through the application.

9. SQLite Database

Stores farmer profile information and feedback.

6. Installation & Execution Steps

Prerequisites

* Python 3.10+
* Node.js 18+
* npm
* Git
* Visual Studio Code

Step 1: Clone the Repository

git clone https://github.com/Saranya2326/Agriadvisory_hackathon.git

Step 2: Navigate to the Project Folder

cd Agriadvisory_hackathon

Step 3: Run the Backend

Open the first terminal.

cd backend

Create a virtual environment:

python -m venv .venv

Activate the environment (Windows PowerShell):

.venv\Scripts\Activate.ps1

Install the required dependencies:

pip install -r requirements.txt

Start the Flask server:

python app.py

Backend URL:

http://127.0.0.1:5000

Step 4: Run the Frontend

Open a second terminal.

cd frontend

Install dependencies:

npm install

Start the development server:

npm run dev

Step 5: Access the Application

Open the local URL displayed in the terminal (usually):

http://localhost:5173

The application is now ready to use.

7. API Endpoints

Method	Endpoint	Purpose
GET	/api/health	Check backend health
POST	/api/farmers	Register farmer
GET	/api/farmers/<id>	Retrieve farmer details
POST	/api/advisory	Get crop advisory
GET	/api/weather	Access weather information
GET	/api/mandi	Access mandi prices
POST	/api/soil-advice	Get basic soil guidance
POST	/api/feedback	Submit feedback

8. Important Notes & Limitations

* This project is a student-built prototype.
* The crop advisory system currently uses predefined rules. It does not train an AI or machine learning model.
* Weather and mandi information may use demo/sample data until official API integrations are configured.
* Sample data must not be treated as real-time official information.
* Weather and market data integrations require valid data-provider access.
* Soil and crop suggestions are general information and should not replace professional agricultural advice.
* External API availability and accuracy depend on the configured data providers.

9. Project Structure

Agriadvisory_hackathon/
│
├── backend/
│   ├── app.py
│   ├── database.py
│   ├── advisory.py
│   ├── services/
│   │   ├── weather_service.py
│   │   └── mandi_service.py
│   ├── requirements.txt
│   └── .env.example
│
├── frontend/
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   └── src/
│       ├── main.jsx
│       ├── App.jsx
│       └── style.css
│
└── README.md

10. Project Goal

To empower Indian farmers by providing accessible, multilingual agricultural information through a simple digital platform and support better-informed farming decisions.
