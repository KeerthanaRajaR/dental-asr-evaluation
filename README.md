# Dental ASR Evaluation Pipeline

## Overview
This project implements an end-to-end evaluation pipeline for Automatic Speech Recognition (ASR) using **Whisper v3 Large Turbo (via Groq)**. The evaluation is performed on realistic **dental doctor–patient conversations**, with a focus on transcription accuracy as well as **clinical safety–critical metrics**.

The objective is to evaluate how well an ASR system preserves medically important information such as terminology, medications, numeric values, laterality, negation, and overall clinical coherence in long-form conversations.

---

## Task Workflow
1. Create realistic dental doctor–patient conversations as ground truth
2. Convert reference text into audio using Text-to-Speech
3. Transcribe audio using Whisper v3 Large Turbo
4. Compare ASR output with reference transcripts
5. Compute standard ASR metrics and clinical safety metrics
6. Automate the workflow for multiple conversations

---

## Implementation Summary
- Reference conversations are manually curated and stored as text files
- Audio is generated using `pyttsx3`
- Long audio is handled using chunked transcription
- ASR is performed using Whisper v3 Large Turbo
- Metrics are computed by comparing ASR output with reference text
- The entire pipeline is automated using a single execution script


---

## Project Structure

dental-asr-evaluation/
│
├── conversations/
│   ├── convo1_reference.txt
│   └── convo2_reference.txt
│
├── audio/
│
├── transcripts/
│   ├── convo1_whisper.txt
│   └── convo2_whisper.txt
│
├── metric/
│   ├── wer_cer_ser.py
│   ├── medical_terms.py
│   ├── medication_accuracy.py
│   ├── numeric_accuracy.py
│   └── laterality_negation.py
│
├── transcribe_utils.py
├── run_all.py
├── requirements.txt
├── .gitignore
└── README.md

## How to Run
```bash
python run_all.py



