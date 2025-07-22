# Reverse Psychology Bot
A Flask-based chatbot that playfully argues against your stated desires using Cohere's text generation API, helping you reflect on your decisions. The bot is deployed on Railway with a modern UI styled using Tailwind CSS.
Table of Contents

## Project Overview
Prerequisites
Setup Instructions
Running Locally
Deploying to Railway
Usage
License

## Project Overview
The Reverse Psychology Bot takes user input (e.g., "I want to go hiking") and responds with a playful counterargument (e.g., "Hiking? Sounds exhausting, and you might get lost!"). It uses:

Flask: Backend web framework.
Cohere API: Generates reverse psychology responses (free tier, no bank details required).
Tailwind CSS: For a clean, responsive UI.
Railway: Hosting platform for deployment (free tier).

The app is live at your-app-name.up.railway.app (replace with your actual Railway URL after deployment).
Prerequisites

Python 3.9+ (download from python.org)
A Cohere API key (sign up at cohere.ai, free tier, no bank details needed)
Git and a GitHub account
Railway account (sign up at railway.app, free tier, no bank details needed)

Setup Instructions

### Clone the Repository:
git clone https://github.com/TanishSharma2004/reverse-psychology-bot
cd reverse-psychology-bot


### Set Up a Virtual Environment:
python -m venv venv

### Activate it:

Windows: venv\Scripts\activate
macOS/Linux: source venv/bin/activate


### Install Dependencies:
pip install -r requirements.txt


### Add Cohere API Key:

Create a .env file in the project root:COHERE_API_KEY=your_actual_api_key_here


Replace your_actual_api_key_here with your key from the Cohere dashboard.



## Running Locally

Run the Flask app:python app.py


Open http://127.0.0.1:5000 in your browser.
Enter a statement (e.g., "I want to learn Python") and see the bot’s response.

## Deploying to Railway

### Push to GitHub:

Ensure .gitignore includes .env, venv/, __pycache__/, and *.pyc.
Commit and push:git add .
git commit -m "Update project for deployment"
git push origin main




### Set Up Railway:

Sign up at railway.app using GitHub.
Create a new project and select your repository.
Add an environment variable in the Railway dashboard:
Key: COHERE_API_KEY
Value: Your Cohere API key.


Deploy the app. Railway uses Procfile (web: gunicorn app:app) and requirements.txt.


### Get the Public URL:

In the Railway dashboard, go to Settings > Generate Domain.
Access your app at the provided URL (e.g., https://your-app-name.up.railway.app).



## Usage

Visit the deployed URL or local server (http://127.0.0.1:5000).
Enter a statement in the input field (e.g., "I want to start a business").
The bot responds with a reverse psychology argument to help you reflect.
Example:
Input: "I want to go hiking"
Output: "Hiking? Why bother with all that effort when you could relax at home?"
