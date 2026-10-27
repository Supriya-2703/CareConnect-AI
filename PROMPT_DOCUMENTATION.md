# CareConnect AI — Prompt Documentation

**Assessment:** AI Skills & Prompt Engineering Assessment  
**Project:** CareConnect AI — Healthcare Information & Appointment Request Prototype  
**Candidate:** Supriya Shahaji Bhade

> Important: This document is a working record/template. Keep only prompts you actually used, and update the revision notes after you test or change the project. Do not claim that an AI tool generated code or results unless that is what happened.

## 1. Project planning prompt

**Prompt**

> I am building a small portfolio project for an AI Growth & Automation Associate assessment. Propose a beginner-friendly healthcare or technology project that demonstrates practical AI use, prompt engineering, problem-solving, and a working prototype. Keep the scope realistic for one person and include a clear demo.

**Purpose**
To narrow the assessment to a project that can be built, tested, and demonstrated.

## 2. Safety and scope prompt

**Prompt**

> Help me define a safe scope for a healthcare information assistant. It must not diagnose, prescribe medication, claim to handle emergencies, or pretend to book real appointments. Add clear disclaimers, privacy guidance, and an emergency escalation message.

**Purpose**
To define safety boundaries before implementation.

## 3. Application implementation prompt

**Prompt**

> Create a beginner-friendly Python Streamlit prototype called CareConnect AI. Include a healthcare information question interface, a simple appointment request form, and local CSV storage. Add optional LLM API integration with a safe system prompt and a local fallback if no API key is configured. Make it clear that appointment requests are not confirmed bookings. Include setup instructions for Windows and VS Code.

**Purpose**
To create the first working version of the application.

## 4. Prompt refinement — safer assistant behavior

**Prompt**

> Refine the assistant system prompt so it only gives general educational information, never diagnoses or prescribes, directs possible emergencies to local emergency services, avoids asking for sensitive information, and keeps answers concise. If the AI API fails, use a transparent local fallback instead of displaying an unhandled error.

**Purpose**
To improve safety, reliability, and user experience.

## 5. Prompt refinement — appointment honesty

**Prompt**

> Review the appointment workflow and make sure the interface clearly says it only saves a local demo request, does not contact a clinic, and does not confirm an appointment. Require user acknowledgment before saving the request.

**Purpose**
To avoid misleading users about what the prototype actually does.

## 6. Testing prompt

**Prompt**

> Create a manual test checklist for CareConnect AI. Include a normal healthcare-navigation question, an emergency-related question, a medication question, an empty appointment form, a valid fictional appointment request, missing API key behavior, and confirmation that the app never claims an appointment is booked.

**Purpose**
To test normal and edge-case behavior before recording the demo.

## 7. Iteration log — fill this in after testing

| Version | What I tested                 | Result observed       | Change made |
| ------- | ----------------------------- | --------------------- | ----------- |
| 1       | Run app without API key       | Fill in after testing | Fill in     |
| 1       | General information question  | Fill in after testing | Fill in     |
| 1       | Emergency-related question    | Fill in after testing | Fill in     |
| 1       | Fictional appointment request | Fill in after testing | Fill in     |

## 8. AI tools disclosure

List only tools actually used:

- ChatGPT: planning, prompt refinement, and/or coding assistance (edit to match actual use).
- Python and Streamlit: application implementation.
- OpenAI API: only if you configure a key and successfully test the AI response mode.
- VS Code: editing and running the project.
