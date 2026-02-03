# 🤖 AI Meeting Assistant Agent

This project is an AI-powered agent designed to streamline post-meeting workflows. Built as part of the **AI Academy**, it leverages the multimodal capabilities of **Gemini 1.5/2.5 Pro** to process meeting audio/video, transcribe content, and automate the creation of professional documentation.

## 🌟 Key Features
- **Multimodal Audio Processing:** Natively analyzes MP3/MP4 files without the need for separate transcription services.
- **Auto-Translation:** Intelligently detects Czech speech and translates it into professional English.
- **Dual-Purpose Output:**
  - **Formal Outlook Draft:** High-level executive summary for meeting participants.
  - **Simplified OneNote Notes:** Clear, easy-to-read "Simple English" notes featuring main ideas, decisions, and a TODO list for personal productivity.

## 🧠 Why an "Agent" and not just an app?
Unlike a static script, this solution acts as an **Agent** by:
1. **Understanding Context:** It adapts its tone based on the target platform (formal for Outlook vs. efficient for OneNote).
2. **Goal-Oriented Behavior:** It doesn't just transcribe; it extracts actionable intelligence (Decisions & Tasks).
3. **Workflow Integration:** It is designed to bridge the gap between raw audio data and professional communication tools.

## 🛠️ Tech Stack
- **Model:** Google Gemini 1.5 Pro / Flash (via Google AI Studio)
- **Language:** Python
- **Integration:** Microsoft 365 (Outlook & OneNote formatting)

## 🚀 How It Works
1. **Input:** The agent receives a meeting recording (MP3/MP4).
2. **Analysis:** Using a specialized **System Prompt**, the agent identifies key speakers, decisions, and action items.
3. **Drafting:** Two distinct versions of the meeting minutes are generated.
4. **Action:** The resulting
