import streamlit as st
import ollama

st.title("ProcessPilot AI")

process_description = st.text_area(
    "Describe a business process",
    placeholder="Example: A customer sends an order by email..."
)

if st.button("Analyze"):
    if not process_description.strip():
        st.warning("Please describe a process first.")
    else:
        with st.spinner("Gemma is analyzing the process..."):
            response = ollama.chat(
                model="gemma4",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are an AI business process consultant. "
                            "Analyze business processes and identify "
                            "automation opportunities."
                        )
                    },
                    {
                        "role": "user",
                        "content": process_description
                    }
                ]
            )

        st.subheader("Gemma's Analysis")
        st.write(response["message"]["content"])