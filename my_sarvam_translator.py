import time
from sarvamai import SarvamAI

def split_text(text, chunk_size=100):
    """
    Split text into chunks of max `chunk_size` words.
    """
    words = text.split()
    return [
        " ".join(words[i:i + chunk_size])
        for i in range(0, len(words), chunk_size)
    ]


def translate_batch(
    texts,
    source_lang="en-IN",
    target_lang="hi-IN",
    chunk_size=100,
    batch_delay=0.5,
    max_retries=5
):
    """
    Translate a list of texts using Sarvam API with:
    - Large chunks
    - Retry on rate-limit
    - Delay after each text batch
    """

    client = SarvamAI(
        # api_subscription_key="sk_osmkn5mp_6uXN4Q1Y1VB7QlQRb0kTADCS"
        # api_subscription_key="sk_eastv3v8_b2jdKeAlffDBSUJMNeQbiB2r"
        api_subscription_key="sk_crc0tk9d_SgfdiLFoR7vi1dnRQ5WuLl5H"
    )

    translated_texts = []

    for idx, text in enumerate(texts, start=1):
        text = text.strip()

        if not text:
            translated_texts.append(text)
            continue

        print(f"\nTranslating text {idx}/{len(texts)}")

        chunks = split_text(text, chunk_size=chunk_size)
        translated_chunks = []

        for chunk_idx, chunk in enumerate(chunks, start=1):
            print(f"   → Chunk {chunk_idx}/{len(chunks)}")

            for attempt in range(max_retries):
                try:
                    resp = client.text.translate(
                        input=chunk,
                        source_language_code="en-IN",
                        target_language_code=target_lang,
                        model="sarvam-translate:v1",
                        speaker_gender="Male",
                    )

                    translated_chunks.append(resp.translated_text)
                    break

                except Exception as e:
                    error_msg = str(e).lower()

                    if "rate" in error_msg or "429" in error_msg:
                        wait_time = 2 ** attempt
                        print(f"Rate limited. Retrying in {wait_time}s...")
                        time.sleep(wait_time)
                    else:
                        print(f"Error: {e}")
                        translated_chunks.append(chunk)
                        break

        final_translation = " ".join(translated_chunks)
        translated_texts.append(final_translation)

        print("Waiting 0.5s before next text...")
        time.sleep(batch_delay)

    return translated_texts