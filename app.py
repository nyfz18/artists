import streamlit as st
import subprocess

def generate_sketch_prompt():
    # Run Ollama CLI and get output
    result = subprocess.run(
        ["ollama", "run", "mistral", "Give me a simple sketch prompt for beginner artists."],
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        return f"Error: {result.stderr}"
    return result.stdout.strip()

st.title("Sketch Muse — AI Sketch Prompt Generator")

if st.button("Generate Prompt"):
    prompt = generate_sketch_prompt()
    st.write("Your sketch prompt:")
    st.write(prompt)
