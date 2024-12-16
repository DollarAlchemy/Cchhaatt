from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Get user input
        user_input = request.json.get("message", "")
        
        if not user_input:
            return jsonify({"error": "No message provided"}), 400

        # GPT-3.5 Turbo API call
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful customer support assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        
        # Get the assistant's reply
        reply = response['choices'][0]['message']['content']
        
        return jsonify({"reply": reply}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
