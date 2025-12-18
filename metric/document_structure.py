import re

def section_heading_accuracy(cid):
    ref = open(f"conversations/convo{cid}_reference.txt", encoding="utf-8").read()
    hyp = open(f"transcripts/convo{cid}_whisper.txt", encoding="utf-8").read()

    heading_pattern = r"(Doctor:|Patient:)"

    ref_headings = re.findall(heading_pattern, ref)
    hyp_headings = re.findall(heading_pattern, hyp)

    correct = sum(1 for r, h in zip(ref_headings, hyp_headings) if r == h)
    total = len(ref_headings)

    accuracy = correct / total if total else 1.0

    print("Section Heading Accuracy:", round(accuracy, 3))
def punctuation_accuracy(cid):
    critical = [".", "?", ":"]

    ref = open(f"conversations/convo{cid}_reference.txt").read()
    hyp = open(f"transcripts/convo{cid}_whisper.txt").read()

    ref_count = sum(ref.count(p) for p in critical)
    hyp_count = sum(hyp.count(p) for p in critical)

    accuracy = min(hyp_count, ref_count) / ref_count if ref_count else 1.0

    print("Punctuation Accuracy (Critical):", round(accuracy, 3))
