import re

def run(cid):
    text = open(f"transcripts/convo{cid}_whisper.txt").read()
    nums = re.findall(r"\d+(?:\.\d+)?", text)
    print("Numbers detected:", nums)
