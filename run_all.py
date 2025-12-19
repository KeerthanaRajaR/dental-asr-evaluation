from pathlib import Path
import pyttsx3

from transcribe_groq import transcribe

from metric import (
    wer_cer_ser,
    medical_terms,
    medication_accuracy,
    numeric_accuracy,
    laterality_negation,
)

from metric.document_structure import section_heading_accuracy, punctuation_accuracy
from metric.semantic_clinical import clinical_coherence_score, ner_f1_score
from metric.system_metrics import *

# ---------------- CONFIG ----------------
FAST_MODE = True   # Set False if you want to re-run transcription
# ----------------------------------------

engine = pyttsx3.init()
engine.setProperty("rate", 170)

for cid in [1, 2]:
    print(f"\n🚀 Conversation {cid}")

    transcript_path = Path(f"transcripts/convo{cid}_whisper.txt")
    audio_path = Path(f"audio/convo{cid}.wav")
    ref_path = Path(f"conversations/convo{cid}_reference.txt")

    # -------- Transcription Step --------
    if FAST_MODE and transcript_path.exists():
        print("⚡ FAST MODE: Using existing transcript")
    else:
        print("🔊 Generating audio & transcription")

        text = ref_path.read_text(encoding="utf-8")

        engine.save_to_file(text, str(audio_path))
        engine.runAndWait()

        transcribe(str(audio_path), str(transcript_path))

    # -------- Metrics --------
    print("📊 METRICS")

    wer_cer_ser.run(cid)
    medical_terms.run(cid)
    medication_accuracy.run(cid)
    numeric_accuracy.run(cid)
    laterality_negation.run(cid)
    laterality_negation.run_negation(cid)

    section_heading_accuracy(cid)
    punctuation_accuracy(cid)
    clinical_coherence_score(cid)
    ner_f1_score(cid)

    transcription_failure_causes(cid)
    partial_transcription_rate(cid)
    audio_quality_proxy(cid)
    confidence_score_proxy(cid)
    flagging_threshold(cid)
    confidence_calibration(cid)
    fp_fn_tradeoff(cid)
    accuracy_speed_tradeoff(cid)

    print("-" * 50)

# -------- System-level Metrics (run once) --------
realtime_vs_batch()
clinical_latency_check()

print("\n🎉 ALL METRICS FOR ALL CONVERSATIONS COMPLETED")
