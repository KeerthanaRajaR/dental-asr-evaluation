import jiwer

def run(cid):
    ref = open(f"conversations/convo{cid}_reference.txt", encoding="utf-8").read()
    hyp = open(f"transcripts/convo{cid}_whisper.txt", encoding="utf-8").read()

    wer = jiwer.wer(ref, hyp)
    cer = jiwer.cer(ref, hyp)

    ref_s = [s for s in ref.split(".") if s.strip()]
    hyp_s = [s for s in hyp.split(".") if s.strip()]

    errors = sum(1 for r, h in zip(ref_s, hyp_s) if jiwer.wer(r, h) > 0)
    ser = errors / min(len(ref_s), len(hyp_s))

    print("WER:", round(wer, 3))
    print("CER:", round(cer, 3))
    print("SER:", round(ser, 3))
