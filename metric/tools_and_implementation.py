from jiwer import wer
import difflib
from collections import Counter
def load_text(cid):
    ref = open(f"conversations/convo{cid}_reference.txt", encoding="utf-8").read().lower()
    hyp = open(f"transcripts/convo{cid}_whisper.txt", encoding="utf-8").read().lower()
    return ref, hyp
def asr_library_consistency(cid):
    ref, hyp = load_text(cid)

    wer_score = wer(ref, hyp)
    consistency = 1 - wer_score

    print("ASR Library Consistency Score:", round(consistency, 3))
def medical_nlp_coverage(cid):
    _, hyp = load_text(cid)

    medical_terms = [
        "infection", "gingivitis", "abscess",
        "paracetamol", "ibuprofen", "lidocaine"
    ]

    detected = sum(1 for t in medical_terms if t in hyp)
    coverage = detected / len(medical_terms)

    print("Medical NLP Coverage Score:", round(coverage, 3))
def string_alignment_score(cid):
    ref, hyp = load_text(cid)

    matcher = difflib.SequenceMatcher(None, ref, hyp)
    score = matcher.ratio()

    print("String Alignment Score:", round(score, 3))
def error_distribution(cid):
    ref, hyp = load_text(cid)

    ref_words = ref.split()
    hyp_words = hyp.split()

    deletions = [w for w in ref_words if w not in hyp_words]
    insertions = [w for w in hyp_words if w not in ref_words]

    summary = {
        "deletions": len(deletions),
        "insertions": len(insertions),
        "top_deleted": Counter(deletions).most_common(3),
        "top_inserted": Counter(insertions).most_common(3),
    }

    print("Error Distribution Summary:", summary)
def cicd_readiness(cid):
    ref, hyp = load_text(cid)

    wer_score = wer(ref, hyp)
    threshold = 0.5

    passed = wer_score < threshold
    print("CI/CD Quality Gate Passed:", passed)
