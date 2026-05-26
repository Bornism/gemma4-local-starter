import ollama
import os

def load_notes(folder):
    notes = []
    for filename in os.listdir(folder):
        if filename.endswith(".txt"):
            filepath = os.path.join(folder, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            notes.append(f"[{filename}]\n{content}")
            print(f"  Loaded: {filename}")
    return "\n\n---\n\n".join(notes)

def ask(question, context):
    print(f"\nQuestion: {question}")
    print("Gemma 4: ", end="", flush=True)

    prompt = f"""You are a helpful assistant with access to a set of personal notes.
Answer the question using ONLY the information in the notes below.
If the answer is not in the notes, say "I don't have that in my notes."
Be concise and direct.

Notes:
{context}

Question: {question}"""

    response = ollama.generate(
        model="gemma4:e4b",
        prompt=prompt,
        stream=True
    )

    for chunk in response:
        print(chunk["response"], end="", flush=True)

    print("\n")

# Load all notes from the folder
print("Loading notes...")
context = load_notes("notes")

# Ask questions across all the notes
ask("What are the key ideas about financial independence?", context)
ask("What did I learn about AI and manufacturing?", context)
ask("What books am I thinking about and why?", context)
ask("What is something I want to build this year?", context)