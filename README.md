# Dental ASR Evaluation using Whisper v3 Large Turbo

## Overview
This project evaluates the performance of Whisper v3 Large Turbo on long-form dental appointment conversations.
The evaluation focuses on both standard ASR metrics and clinical safety-critical metrics.

## Workflow
1. Create realistic dental doctor–patient conversations (ground truth)
2. Convert text to audio using pyttsx3
3. Transcribe audio using Whisper v3 Large Turbo via Groq
4. Compare ASR output with reference transcripts
5. Compute evaluation metrics

## Metrics Implemented
- Word Error Rate (WER)
- Character Error Rate (CER)
- Sentence Error Rate (SER)
- Medical Terminology Accuracy
- Medication Accuracy
- Numeric Accuracy
- Laterality Accuracy
- Negation Accuracy

## Technologies Used
- Python
- pyttsx3 (Text-to-Speech)
- Whisper v3 Large Turbo (Groq)
- jiwer
- Regex

## How to Run
```bash
python run_all.py
