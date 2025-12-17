import re

def run(cid):
    meds = re.findall(r"(paracetamol|ibuprofen|lidocaine|clindamycin)", 
                      open(f"transcripts/convo{cid}_whisper.txt").read().lower())
    print("Medications detected:", list(set(meds)))
