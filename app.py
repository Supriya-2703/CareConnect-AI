import os
import csv
from datetime import date, time, datetime
from pathlib import Path

import streamlit as st

APP_TITLE = "CareConnect AI"
DATA_DIR = Path("data")
APPOINTMENTS_FILE = DATA_DIR / "appointment_requests.csv"

st.set_page_config(page_title=APP_TITLE, page_icon="🩺", layout="wide")

SAFE_INFO = {
    "appointments": "You can submit an appointment request using the form. This demo records a request only; it does not confirm a real appointment.",
    "hours": "Opening hours depend on the clinic. Please contact your chosen clinic directly to confirm its hours.",
    "emergency": "If you may be experiencing a medical emergency, contact your local emergency number or go to the nearest emergency department now.",
    "medication": "I can’t recommend a medication or dosage. Please ask a licensed clinician or pharmacist who knows your situation.",
    "symptoms": "I can share general health information, but I can’t diagnose symptoms. If symptoms are severe, sudden, or worsening, seek urgent medical care.",
    "privacy": "This prototype stores appointment requests locally in a CSV file. Do not enter medical records, government IDs, payment details, or other sensitive information.",
    "general": "I can help with general healthcare information and appointment-request steps. I can’t diagnose conditions, interpret emergencies, or recommend specific treatment."
}

def local_answer(question: str) -> str:
    q = question.lower()
    if any(word in q for word in ["emergency", "chest pain", "can't breathe", "cannot breathe", "severe bleeding"]):
        return SAFE_INFO["emergency"]
    if any(word in q for word in ["medicine", "medication", "dosage", "tablet", "antibiotic", "prescription"]):
        return SAFE_INFO["medication"]
    if any(word in q for word in ["symptom", "pain", "fever", "diagnose", "diagnosis", "rash", "cough"]):
        return SAFE_INFO["symptoms"]
    if any(word in q for word in ["appointment", "book", "schedule", "doctor", "clinic"]):
        return SAFE_INFO["appointments"]
    if any(word in q for word in ["privacy", "data", "stored", "save", "personal information"]):
        return SAFE_INFO["privacy"]
    if any(word in q for word in ["hour", "open", "opening", "close", "closing"]):
        return SAFE_INFO["hours"]
    return SAFE_INFO["general"]

def get_ai_answer(question: str) -> tuple[str, str]:
    """Use OpenAI if configured; otherwise use the transparent local fallback."""
    api_key = os.getenv("OPENAI_API_KEY", "").strip()
    if not api_key:
        return local_answer(question), "Local safe-response mode (no API key configured)"
    try:
        from openai import OpenAI
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            temperature=0.2,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are CareConnect AI, a cautious healthcare information and appointment assistant. "
                        "Give only general educational information, in plain language. Never diagnose, prescribe, "
                        "recommend medication doses, or claim to book/confirm an appointment. For possible emergencies, "
                        "tell the user to contact local emergency services or go to an emergency department. "
                        "Encourage consulting a licensed healthcare professional for personal medical advice. "
                        "Do not request sensitive personal or medical data. Keep answers concise."
                    ),
                },
                {"role": "user", "content": question[:1500]},
            ],
        )
        answer = response.choices[0].message.content or SAFE_INFO["general"]
        return answer, "AI response mode"
    except Exception:
        return local_answer(question), "Local fallback mode (AI service unavailable)"

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("🩺 CareConnect AI")
st.caption("Healthcare information helper + appointment request prototype")
st.info(
    "Prototype only: this is not a medical service and does not diagnose or treat conditions. "
    "Appointment requests are not real bookings. Do not enter sensitive medical information."
)

tab_chat, tab_appointment, tab_about = st.tabs(
    ["💬 Ask a question", "📅 Request an appointment", "ℹ️ About & safety"]
)

with tab_chat:
    st.subheader("General healthcare information")
    st.write("Ask about general healthcare navigation, appointment steps, privacy, or how to seek care.")
    with st.form("question_form", clear_on_submit=True):
        question = st.text_area(
            "Your question",
            placeholder="Example: What information should I prepare before requesting a clinic appointment?",
            max_chars=1500,
        )
        submitted = st.form_submit_button("Get response", type="primary")
    if submitted:
        if not question.strip():
            st.warning("Please enter a question.")
        else:
            answer, mode = get_ai_answer(question.strip())
            st.session_state.chat_history.append(
                {"question": question.strip(), "answer": answer, "mode": mode}
            )
    for item in reversed(st.session_state.chat_history):
        with st.container(border=True):
            st.markdown(f"**You asked:** {item['question']}")
            st.markdown(f"**CareConnect AI:** {item['answer']}")
            st.caption(item["mode"])

with tab_appointment:
    st.subheader("Appointment request")
    st.write("This form saves a request to a local CSV file for demonstration. It does not contact a clinic.")
    with st.form("appointment_form", clear_on_submit=True):
        name = st.text_input("Name or preferred contact name", max_chars=80)
        contact = st.text_input("Contact email or phone (demo data only)", max_chars=120)
        appointment_date = st.date_input("Preferred date", min_value=date.today())
        preferred_time = st.selectbox(
            "Preferred time",
            ["Morning (9 AM–12 PM)", "Afternoon (12 PM–4 PM)", "Evening (4 PM–7 PM)", "Flexible"],
        )
        reason = st.selectbox(
            "Request type (do not include symptoms)",
            ["General consultation", "Follow-up", "Routine check-up", "Other"],
        )
        consent = st.checkbox("I understand this is a demo request and is not a confirmed booking.")
        submitted_request = st.form_submit_button("Save demo request", type="primary")
    if submitted_request:
        if not name.strip() or not contact.strip():
            st.error("Please enter a name and contact detail for this demo.")
        elif not consent:
            st.error("Please confirm that you understand this is only a demo request.")
        else:
            DATA_DIR.mkdir(exist_ok=True)
            new_file = not APPOINTMENTS_FILE.exists()
            with APPOINTMENTS_FILE.open("a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                if new_file:
                    writer.writerow(["created_at", "name", "contact", "preferred_date", "preferred_time", "request_type"])
                writer.writerow([
                    datetime.now().isoformat(timespec="seconds"),
                    name.strip(),
                    contact.strip(),
                    appointment_date.isoformat(),
                    preferred_time,
                    reason,
                ])
            st.success("Demo request saved locally. No clinic has been contacted and no appointment is confirmed.")
            st.caption(f"Local file: {APPOINTMENTS_FILE.as_posix()}")

with tab_about:
    st.subheader("What this prototype demonstrates")
    st.markdown(
        "- AI-assisted general information with a safety-focused system prompt.\n"
        "- A local fallback when an AI API key is not configured.\n"
        "- Appointment request capture and local CSV storage.\n"
        "- Clear disclosure that requests are not real bookings."
    )
    st.subheader("Safety and privacy")
    st.markdown(
        "- Do not use this app for emergencies or diagnosis.\n"
        "- Do not enter symptoms, medical records, insurance details, IDs, or payment data into the appointment form.\n"
        "- The demo saves contact details locally in `data/appointment_requests.csv`; delete this file after testing.\n"
        "- If you configure an external AI API, the question you submit is sent to that provider for processing."
    )
    st.subheader("Suggested demo questions")
    st.markdown(
        "- What should I prepare before requesting an appointment?\n"
        "- Can you diagnose a fever?\n"
        "- What should I do if I think this is an emergency?\n"
        "- How does this demo handle appointment requests?"
    )

st.divider()
st.caption("CareConnect AI • Student portfolio prototype • Not for clinical use")
