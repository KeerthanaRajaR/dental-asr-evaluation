def clinical_coherence_score(cid):
    hyp = open(f"transcripts/convo{cid}_whisper.txt").read().lower()

    symptoms = ["pain", "swelling", "fever"]
    diagnosis = ["infection", "gingivitis", "pulpitis", "abscess"]
    treatment = ["scaling", "root canal", "extraction", "paracetamol", "ibuprofen"]

    symptom_found = any(s in hyp for s in symptoms)
    diagnosis_found = any(d in hyp for d in diagnosis)
    treatment_found = any(t in hyp for t in treatment)

    score = sum([symptom_found, diagnosis_found, treatment_found]) / 3

    print("Clinical Coherence Score:", round(score, 3))
def ner_f1_score(cid):
    medical_entities = [
        "infection", "gingivitis", "pulpitis", "abscess",
        "paracetamol", "ibuprofen", "lidocaine"
    ]

    ref = open(f"conversations/convo{cid}_reference.txt").read().lower()
    hyp = open(f"transcripts/convo{cid}_whisper.txt").read().lower()

    ref_entities = {e for e in medical_entities if e in ref}
    hyp_entities = {e for e in medical_entities if e in hyp}

    tp = len(ref_entities & hyp_entities)
    fp = len(hyp_entities - ref_entities)
    fn = len(ref_entities - hyp_entities)

    precision = tp / (tp + fp) if (tp + fp) else 1.0
    recall = tp / (tp + fn) if (tp + fn) else 1.0

    f1 = (2 * precision * recall) / (precision + recall) if (precision + recall) else 0

    print("NER F1 Score:", round(f1, 3))
