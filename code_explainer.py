import ollama
import argparse

def explain_code(file_path, model="codellama"):
    with open(file_path, "r") as file:
        code = file.read()

    prompt = f"Explain the following Python code in simple terms:\n\n{code}\n\nProvide a clear, beginner-friendly explanation."

    response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])

    print("\n💡 AI Explanation:\n")
    print(response["message"]["content"])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI-Based Code Explainer")
    parser.add_argument("file", help="Path to the Python script to explain")
    parser.add_argument("--model", choices=["codellama", "mistral"], default="codellama", help="Choose the AI model")
    args = parser.parse_args()

    explain_code(args.file, args.model)
