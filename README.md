# Gen_AI_Chatbot
This project implements a simple web application using Flask and the Google Gemini API to generate professional emails based on user input. The application consists of a backend (written in Python using Flask) and a frontend (implemented using HTML, CSS, and JavaScript).

# Email Chatbot using Flask and Google Gemini API

This project is a simple web application that allows users to generate professional emails using the Google Gemini API. Users can input their name, email, tax ID, and the desired subject of the email. The application then uses the Gemini API to generate a two-paragraph email body and a polite closing statement, formatted as a professional email.

## Prerequisites

Before you begin, ensure you have the following installed:

* **Python 3.6 or higher:** You can download it from [python.org](https://www.python.org/).
* **pip:** Python package installer, usually included with Python.
* **Google Cloud Project:** You need a Google Cloud Project with the Gemini API enabled.
* **Google Gemini API Key:** You will need to generate an API key for your Google Cloud Project. You can find instructions on how to do this in the [Google Cloud documentation](https://makersuite.google.com/app/apikey).
* **Git:** For version control and cloning the repository. You can download it from [git-scm.com](https://git-scm.com/).

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <your_repository_url>
    cd <your_project_name>
    ```
    *(Replace `<your_repository_url>` with the actual URL of your GitHub repository and `<your_project_name>` with the name of your project directory.)*

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ```
    On Windows:
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    On Linux/macOS:
    ```bash
    source venv/bin/activate
    ```
    On Windows:
    ```bash
    venv\Scripts\activate
    ```

4.  **Install the required Python packages:**
    ```bash
    pip install -r requirements.txt
    ```
    *(You'll need to create a `requirements.txt` file listing the project dependencies. For this project, it should contain at least `Flask` and `google-generativeai`.)*
    Create a file named `requirements.txt` in your project's root directory and add the following lines:
    ```
    Flask
    google-generativeai
    ```

5.  **Set your Google Gemini API Key:**
    You need to replace the placeholder API key in your `app.py` file with your actual API key. Open `app.py` and find the line:
    ```python
    genai.configure(api_key="AIzaSyAOngoVqGTtCi9upt6cGfCgDdfeLuNJdNE")  # Replace with your actual API key
    ```
    Replace `"AIzaSyAOngoVqGTtCi9upt6cGfCgDdfeLuNJdNE"` with your actual Gemini API key.

    **Important Security Note:** For production applications, it is highly recommended to store your API key as an environment variable or use a more secure method instead of hardcoding it directly in the code.

## Running the Application

1.  **Navigate to the project directory:**
    ```bash
    cd <your_project_name>
    ```

2.  **Activate the virtual environment (if you haven't already):**
    On Linux/macOS:
    ```bash
    source venv/bin/activate
    ```
    On Windows:
    ```bash
    venv\Scripts\activate
    ```

3.  **Run the Flask development server:**
    ```bash
    python app.py
    ```

4.  **Open your web browser:**
    Go to `http://127.0.0.1:5000/` in your web browser. You should see the "Generate Professional Email" interface.

## Usage

1.  Enter your name in the "Your Name" field.
2.  Enter your email address in the "Your Email" field.
3.  Enter your tax ID in the "Your Tax ID" field.
4.  Enter the desired subject of your email in the "Email Subject" textarea.
5.  Click the "Generate Email" button.
6.  The generated email will appear in the "Generated Email" section below the form.
7.  You can click the "Copy to Clipboard" button to copy the generated email text.
8.  Click the "Clear Form" button to reset the input fields.
9.  Use the "↑ Top" button to quickly scroll back to the top of the page.

## Important Notes

* This is a basic implementation for demonstration purposes. For production use, consider implementing more robust error handling, input validation, and security measures.
* Ensure you have reviewed and understand the terms of service for the Google Gemini API.
* Be mindful of the costs associated with using the Google Gemini API, as usage beyond a certain free tier may incur charges.

## Contributing

If you'd like to contribute to this project, please feel free to fork the repository and submit a pull request with your changes.
For any queries contact : bhanududikatla@gmail.com
