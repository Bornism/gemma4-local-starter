import ollama

def chat(prompt):
    print(f"\nYou: {prompt}")
    print("Gemma 4: ", end="", flush=True)
    
    response = ollama.generate(
        model="gemma4:e4b",
        prompt=prompt,
        stream=True
    )
    
    for chunk in response:
        print(chunk["response"], end="", flush=True)
    
    print("\n")

# Demo prompts
chat("What is a large language model? Explain it in 3 sentences.")
chat("What is the difference between a CPU and a GPU for AI inference?")
chat("Why would a company want to run an AI model locally instead of using a cloud API?")