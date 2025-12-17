from groq import Groq
import os
import wave

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def split_wav(input_wav, chunk_seconds=180):
    with wave.open(input_wav, 'rb') as wf:
        rate = wf.getframerate()
        frames_per_chunk = rate * chunk_seconds
        params = wf.getparams()

        chunks = []
        i = 0
        while True:
            frames = wf.readframes(frames_per_chunk)
            if not frames:
                break

            name = f"audio/tmp_chunk_{i}.wav"
            with wave.open(name, 'wb') as out:
                out.setparams(params)
                out.writeframes(frames)

            chunks.append(name)
            i += 1
        return chunks


def transcribe(audio_path, output_txt):
    chunks = split_wav(audio_path)
    final_text = ""

    for i, chunk in enumerate(chunks):
        print(f"   🔹 Transcribing chunk {i+1}/{len(chunks)}")
        with open(chunk, "rb") as f:
            t = client.audio.transcriptions.create(
                file=f,
                model="whisper-large-v3-turbo"
            )
            final_text += t.text + " "

    with open(output_txt, "w", encoding="utf-8") as out:
        out.write(final_text)

    print("   ✅ Transcription done\n")
