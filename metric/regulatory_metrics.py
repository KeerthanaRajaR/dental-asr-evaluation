import re
def load_text(cid):
    ref = open(f"conversations/convo{cid}_reference.txt", encoding="utf-8").read().lower()
    hyp = open(f"transcripts/convo{cid}_whisper.txt", encoding="utf-8").read().lower()
    return ref, hyp
def phi_exposure_risk(cid):
    _, hyp = load_text(cid)

    phi_patterns = [
        r"\b\d{10}\b",          # phone-like numbers
        r"\b\d{2}/\d{2}/\d{4}\b",  # date
        "mr.", "mrs.", "patient name"
    ]

    leaks = sum(1 for p in phi_patterns if re.search(p, hyp))
    risk = 1 - min(leaks / 3, 1)

    print("PHI Exposure Risk Score:", round(risk, 3))
def clinical_safety_stability(cid):
    ref, hyp = load_text(cid)

    critical = ["infection", "abscess", "paracetamol", "ibuprofen"]
    preserved = sum(1 for c in critical if c in ref and c in hyp)

    score = preserved / len(critical)
    print("Clinical Safety Stability Score:", round(score, 3))
def transcription_standards_compliance(cid):
    _, hyp = load_text(cid)

    checks = {
        "numbers": any(char.isdigit() for char in hyp),
        "medical_terms": any(t in hyp for t in ["infection", "gingivitis", "abscess"]),
        "punctuation": "." in hyp
    }

    score = sum(checks.values()) / len(checks)
    print("Transcription Standards Compliance Score:", round(score, 3))
def documentation_clarity(cid):
    _, hyp = load_text(cid)

    negations = ["no", "not", "denies"]
    ambiguity = ["maybe", "possibly", "unclear"]

    neg_ok = any(n in hyp for n in negations)
    ambiguous = any(a in hyp for a in ambiguity)

    score = 1.0 if neg_ok and not ambiguous else 0.7
    print("Clinical Documentation Clarity Score:", round(score, 3))
