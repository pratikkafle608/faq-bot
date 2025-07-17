 FAQ Bot
An intelligent FAQ chatbot built with a Flask backend and a React frontend. This project allows users to ask questions through a web interface and receive helpful responses powered by customizable backend logic (e.g., keyword matching, AI APIs, or database lookups).

🏗️ Project Structure
php
Copy
Edit
faq-bot/
├── backend/          # Flask API (Python)
│   └── app.py        # Main server logic
│   └── venv/         # Python virtual environment (not uploaded to Git)
├── frontend/         # React app (JavaScript)
│   └── src/          # React components
│   └── public/       # Static files
│   └── tailwind.config.js
└── README.md         # Project description
🚀 Features
✅ Ask questions via a simple web interface

✅ Backend API built with Flask

✅ Frontend UI styled using Tailwind CSS

✅ Uses Lucide React for clean modern icons

✅ CORS enabled for frontend-backend communication

✅ Easily extendable to integrate with OpenAI, database queries, or custom logic

🛠️ Tech Stack
Frontend: React, Tailwind CSS, Lucide React

Backend: Python, Flask, Flask-CORS

Tooling: PostCSS, Node.js, Virtualenv

📦 Setup Instructions
Backend:
bash
Copy
Edit
cd backend
python -m venv venv
venv\Scripts\activate    # Or source venv/bin/activate on macOS/Linux
pip install flask flask-cors
python app.py
Frontend:
bash
Copy
Edit
cd frontend
npm install
npm start
