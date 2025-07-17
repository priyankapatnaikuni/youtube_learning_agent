import streamlit as st
from agents.summary_agent import generate_summary
from agents.notes_agent import generate_notes
from agents.flashcard_agent import generate_flashcards
from agents.quiz_agent import generate_quiz

st.title("🎓 YouTube Learning Agent")

url = st.text_input("Enter a YouTube Video URL")

if url:
    with st.spinner("Generating learning materials..."):

        summary = generate_summary(url)
        notes = generate_notes(url)
        flashcards = generate_flashcards(url, count=5)
        quiz = generate_quiz(url, count=5)

    st.subheader("📄 Summary")
    st.write(summary)

    st.subheader("📝 Notes")
    st.markdown(notes)

    st.subheader("🧠 Flashcards")
    for i, card in enumerate(flashcards, 1):
        with st.expander(f"Q{i}: {card['question']}"):
            st.write(f"A: {card['answer']}")

    st.subheader("❓ Quiz")
    for i, q in enumerate(quiz, 1):
        st.write(f"**Q{i}: {q['question']}**")
        if q.get("options"):
            for opt in q["options"]:
                st.write(f"- {opt}")
        st.write(f"**Answer:** {q['answer']}")