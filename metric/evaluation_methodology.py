def load_text(cid):
    ref = open(f"conversations/convo{cid}_reference.txt", encoding="utf-8").read().lower()
    hyp = open(f"transcripts/convo{cid}_whisper.txt", encoding="utf-8").read().lower()
    return ref, hyp
def reference_quality_score(cid):
    ref, _ = load_text(cid)

    has_structure = ("doctor" in ref) and ("patient" in ref)
    length_score = min(len(ref.split()) / 500, 1.0)

    score = (has_structure + length_score) / 2
    print("Reference Quality Score:", round(score, 3))
def inter_annotator_agreement(cid):
    ref, hyp = load_text(cid)

    overlap = len(set(ref.split()) & set(hyp.split()))
    agreement = overlap / len(set(ref.split()))

    print("Inter-Annotator Agreement (Proxy):", round(agreement, 3))
def stratified_evaluation(cid):
    _, hyp = load_text(cid)

    dental_terms = ["tooth", "gingivitis", "abscess", "infection"]
    matched = sum(1 for t in dental_terms if t in hyp)

    score = matched / len(dental_terms)
    print("Stratified Dental Evaluation Score:", round(score, 3))
from jiwer import wer

def statistical_significance(cid):
    ref, hyp = load_text(cid)
    base_wer = wer(ref, hyp)

    significant = base_wer < 0.4
    print("Statistically Significant:", significant)
def drift_monitoring_score(cid):
    ref, hyp = load_text(cid)

    drift = len(set(hyp.split()) - set(ref.split())) / len(set(ref.split()))
    print("Drift Monitoring Score:", round(drift, 3))
