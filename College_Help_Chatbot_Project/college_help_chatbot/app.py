"""Browser interface for College Help Chatbot. Deploy with Streamlit."""
import streamlit as st
from chatbot import get_response

st.set_page_config(page_title="College Help Chatbot", page_icon="🎓", layout="centered")

st.title("🎓 College Help Chatbot")
st.caption("A simple rule-based assistant for common college questions")
st.info("This demo uses fixed keyword rules. College-specific details should be confirmed with your official college office.")

with st.sidebar:
    st.header("Quick questions")
    st.write("Click a topic to see a sample answer.")
    quick_questions = {
        "Admissions": "How do I apply for admission?",
        "Courses": "What courses are available?",
        "Fees": "How can I check college fees?",
        "Exams": "Where can I find the exam timetable?",
        "Library": "How does the library work?",
        "Placements": "Tell me about placements and internships.",
    }
    for topic, question in quick_questions.items():
        if st.button(topic, use_container_width=True):
            st.session_state.pending_question = question
    if st.button("Clear conversation", use_container_width=True):
        st.session_state.messages = []
        st.session_state.pending_question = None
        st.rerun()

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! Welcome to College Help Chatbot. Ask about admissions, courses, fees, exams, attendance, library, scholarships, hostel, transport, or placements. Type 'help' to see the topics."}
    ]
if "pending_question" not in st.session_state:
    st.session_state.pending_question = None

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ask a college-related question...")
if st.session_state.pending_question:
    prompt = st.session_state.pending_question
    st.session_state.pending_question = None

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    reply = get_response(prompt)
    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.rerun()

st.divider()
st.caption("Rule-based demo project | Python if/elif/else | No AI API required")
