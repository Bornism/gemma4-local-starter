import ollama
import os

def summarize(filepath):
    # Read the document
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    word_count = len(content.split())
    print(f"\nDocument: {filepath}")
    print(f"Word count: {word_count}")
    print(f"Summarizing...\n")

    prompt = f"""You are a helpful assistant. Read the following document and provide:
1. A 3-sentence summary
2. The 3 most important takeaways as bullet points
3. One question this document leaves unanswered

Document:
{content}"""

    print("Gemma 4: ", end="", flush=True)

    response = ollama.generate(
        model="gemma4:e4b",
        prompt=prompt,
        stream=True
    )

    for chunk in response:
        print(chunk["response"], end="", flush=True)

    print("\n")

# Run it
summarize("sample.txt")