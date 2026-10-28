<<<<<<< HEAD
# CareConnect AI

A small healthcare information and appointment-request prototype built with Python and Streamlit for the Gokul Infocare AI Skills & Prompt Engineering Assessment.

## Features
- General healthcare navigation responses with a safety-focused AI system prompt.
- Safe local fallback when no OpenAI API key is configured.
- Appointment request form that saves demo requests to a local CSV file.
- Clear warnings: no diagnosis, treatment, emergency handling, or real appointment booking.

## Requirements
- Python 3.10+
- Internet connection to install dependencies
- Optional OpenAI API key for AI responses

## Run locally (Windows / VS Code)
1. Extract this folder.
2. Open it in VS Code.
3. Open Terminal in VS Code.
4. Create a virtual environment:
   ```powershell
   python -m venv .venv
   ```
5. Activate it:
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```
6. Install packages:
   ```powershell
   python -m pip install -r requirements.txt
   ```
7. Run the app:
   ```powershell
   python -m streamlit run app.py
   ```

The app should open in your browser. It works in local fallback mode without an API key.

## Optional AI setup
Set environment variables in the terminal before launching. Do not put secrets in `app.py` or commit them to GitHub.

```powershell
$env:OPENAI_API_KEY="YOUR_KEY_HERE"
$env:OPENAI_MODEL="gpt-4o-mini"
python -m streamlit run app.py
```

An API key may incur charges depending on your account and provider settings. If you do not have a key, use the local fallback and explain that honestly in your presentation.

## Test checklist
- Ask a general question and verify a response appears.
- Ask about a possible emergency and confirm it advises contacting emergency services.
- Submit an appointment request using clearly fictional demo details.
- Confirm the success message says it is not a confirmed booking.
- Check that `data/appointment_requests.csv` is created.
- Delete the CSV after testing if it contains any personal information.

## Privacy and safety
This is an educational prototype, not a medical device or clinical service. Never use it for real patient information. The local CSV may contain contact details entered during a demo; use fictional data and delete it after testing. Questions submitted while using an external AI provider may be processed by that provider.

## Project structure
```text
ai_healthcare_assistant/
├── app.py
├── requirements.txt
├── .env.example
├── README.md
├── PROMPT_DOCUMENTATION.md
├── VIDEO_PRESENTATION_SCRIPT.md
└── SUBMISSION_EMAIL.md
```
=======
# CareConnect-AI
>>>>>>> b217b51d7cdfe6ee41687f65e24c65359f8e3882
