from flask import Flask, request, jsonify, render_template
import google.generativeai as genai

app = Flask(__name__)

# Set your Google Gemini API Key
genai.configure(api_key="AIzaSyAOngoVqGTtCi9upt6cGfCgDdfeLuNJdNE")  # Replace with your actual API key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-email', methods=['POST'])
def generate_email():
    data = request.json
    name = data.get("name")
    email = data.get("email")
    taxid = data.get("taxid")
    subject = data.get("subject")

    if not all([name, email, taxid, subject]):
        return jsonify({"error": "All fields are required (name, email, taxid, subject)"}), 400

    try:
        # Use the correct model name
        model = genai.GenerativeModel("models/gemini-1.5-pro")  
        prompt = f"""
        Generate a professional email with the following structure:

        - **Subject:** {subject}
        - **Body:** (2 paragraphs explaining the subject)
        - **Footer:** (A polite closing statement)

        User details:
        Name: {name}
        Email: {email}
        Tax ID: {taxid}
        """

        response = model.generate_content(prompt)

        # Ensure the response is a valid JSON-friendly format
        if hasattr(response, "text"):
            email_content = response.text.replace("\n", "<br>")  # Preserve formatting for HTML display
            return jsonify({"response": email_content})
        else:
            return jsonify({"error": "Failed to generate a response"}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
