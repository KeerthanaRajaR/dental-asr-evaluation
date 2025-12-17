from pathlib import Path
import pyttsx3

from transcribe_groq import transcribe
from metric import (
    wer_cer_ser,
    medical_terms,
    medication_accuracy,
    numeric_accuracy,
    laterality_negation
)

FAST_MODE = True   # 🔥 change to False if you want full run

engine = pyttsx3.init()
engine.setProperty("rate", 170)

for cid in [1, 2]:
    print(f"\n🚀 Conversation {cid}")

    transcript_path = f"transcripts/convo{cid}_whisper.txt"

    # 🔴 Only generate audio + transcription when needed
    if not FAST_MODE or cid == 1 or not Path(transcript_path).exists():
        print("🔊 Generating audio & transcription")

        text = Path(f"conversations/convo{cid}_reference.txt").read_text(encoding="utf-8")
        audio_path = f"audio/convo{cid}.wav"

        engine.save_to_file(text, audio_path)
        engine.runAndWait()

        transcribe(audio_path, transcript_path)

    else:
        print("⚡ FAST MODE: Using existing transcript")

    # 🟢 Metrics always run
    print("📊 METRICS")
    wer_cer_ser.run(cid)
    medical_terms.run(cid)
    medication_accuracy.run(cid)
    numeric_accuracy.run(cid)
    laterality_negation.run(cid)
    laterality_negation.run_negation(cid)


    print("-" * 50)

print("\n🎉 ALL METRICS FOR ALL CONVERSATIONS COMPLETED")
