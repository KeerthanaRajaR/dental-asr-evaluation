def load_text(cid):
    ref = open(f"conversations/convo{cid}_reference.txt", encoding="utf-8").read().lower()
    hyp = open(f"transcripts/convo{cid}_whisper.txt", encoding="utf-8").read().lower()
    return ref, hyp
def weighted_error_rate(cid):
    ref, hyp = load_text(cid)

    weights = {
        "medication": 10.0,
        "number": 5.0,
        "laterality": 5.0,
        "general": 1.0
    }

    medication_terms = ["paracetamol", "ibuprofen", "lidocaine"]
    laterality_terms = ["left", "right"]

    ref_words = ref.split()
    hyp_words = hyp.split()

    weighted_errors = 0
    total_weight = 0

    for w in ref_words:
        if w in medication_terms:
            weight = weights["medication"]
        elif w.isdigit():
            weight = weights["number"]
        elif w in laterality_terms:
            weight = weights["laterality"]
        else:
            weight = weights["general"]

        total_weight += weight
        if w not in hyp_words:
            weighted_errors += weight

    score = weighted_errors / total_weight if total_weight else 0
    print("Weighted Error Rate:", round(score, 3))
def error_weight_distribution(cid):
    ref, hyp = load_text(cid)

    categories = {
        "medication": ["paracetamol", "ibuprofen", "lidocaine"],
        "laterality": ["left", "right"],
        "number": []
    }

    distribution = {"medication": 0, "laterality": 0, "number": 0, "general": 0}

    for word in ref.split():
        if word.isdigit():
            distribution["number"] += 1
        elif word in categories["medication"]:
            distribution["medication"] += 1
        elif word in categories["laterality"]:
            distribution["laterality"] += 1
        else:
            distribution["general"] += 1

    print("Error Category Distribution:", distribution)
def clinical_severity_score(cid):
    ref, hyp = load_text(cid)

    critical_terms = ["paracetamol", "ibuprofen", "lidocaine", "left", "right"]

    missed = [t for t in critical_terms if t in ref and t not in hyp]
    severity = 1 - (len(missed) / len(critical_terms)) if critical_terms else 1.0

    print("Clinical Severity Preservation Score:", round(severity, 3))
def clinical_validation_readiness(cid):
    ref, hyp = load_text(cid)

    essential = ["infection", "pain", "treatment"]
    preserved = sum(1 for e in essential if e in hyp)

    readiness = preserved / len(essential)
    print("Clinical Validation Readiness:", round(readiness, 3))
