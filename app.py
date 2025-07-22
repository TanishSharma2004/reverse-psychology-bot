from flask import Flask, render_template, request
import cohere
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # For CSRF protection

# Initialize Cohere client with API key from environment variable
cohere_api_key = os.getenv('COHERE_API_KEY')
if not cohere_api_key:
    raise ValueError("COHERE_API_KEY environment variable not set")
co = cohere.Client(cohere_api_key)

@app.route('/', methods=['GET', 'POST'])
def home():
    bot_response = ""
    user_input = ""
    
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        if user_input:
            # Craft prompt for reverse psychology
            prompt = f"The user says: '{user_input}'. Respond with a playful, reverse psychology argument against it to help them reflect on their decision."
            try:
                response = co.generate(
                    model='command',
                    prompt=prompt,
                    max_tokens=100,
                    temperature=0.7
                )
                bot_response = response.generations[0].text.strip()
            except Exception as e:
                bot_response = f"Error: Could not generate response. {str(e)}"
    
    return render_template('index.html', bot_response=bot_response, user_input=user_input)

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)