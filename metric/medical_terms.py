def run(cid):
    medical_terms = [
        "gingivitis", "pulpitis", "abscess",
        "scaling", "wisdom tooth",
        "root canal", "infection"
    ]

    ref = open(f"conversations/convo{cid}_reference.txt", encoding="utf-8").read().lower()
    hyp = open(f"transcripts/convo{cid}_whisper.txt", encoding="utf-8").read().lower()

    ref_terms = {t for t in medical_terms if t in ref}
    hyp_terms = {t for t in medical_terms if t in hyp}

    correct = ref_terms.intersection(hyp_terms)

    accuracy = len(correct) / len(ref_terms) if ref_terms else 1.0

    print("Medical Terminology Accuracy:", round(accuracy, 3))
    print("  Reference terms:", list(ref_terms))
    print("  Correctly transcribed:", list(correct))
