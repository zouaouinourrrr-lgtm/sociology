import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(page_title="Social Breakdown Quiz", page_icon="🧪")

# Custom Styling
st.markdown("""
    <style>
    .main-title { color: #ad1457; text-align: center; font-size: 40px; font-weight: bold; }
    .subtitle { text-align: center; font-style: italic; color: #555; margin-bottom: 30px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="main-title">SOCIAL BREAKDOWN QUIZ</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Analyzing the Socialization of Nour & Houda</div>', unsafe_allow_html=True)

# 2. Your 10 Specific Phrases
phrases = [
    "I have a 'Home Voice' and a 'Public Voice' that sound like two completely different people.",
    "The sound of a school bell or a loud timer triggers an immediate, unexplainable spike of anxiety in my chest.",
    "My childhood toy box was strictly 'color-coded' and filled with objects society decided were right for my gender.",
    "I have accidentally raised my hand to ask for permission to speak during a family dinner or a night out with friends.",
    "I feel an intense wave of guilt and panic if I am even two minutes late for an appointment.",
    "I have accidentally called a teacher 'Mom' or 'Dad' because my brain confused the two main 'bosses' in my life.",
    "I catch myself calculating my entire value as a human being based solely on my GPA or my exam results.",
    "I have physically hidden behind a shelf in a supermarket just to avoid having to talk to a professor in the 'real world'.",
    "My family has a secret set of 'unspoken rules' and traditions that would make absolutely no sense to any outsider.",
    "I automatically sit in the same unassigned chair every single day because my brain is socialized to crave order and hierarchy."
]

# 3. The Quiz Interface
with st.form("quiz_form"):
    st.write("### Select all that apply:")
    
    # Store results in a list
    checks = []
    for phrase in phrases:
        checks.append(st.checkbox(phrase))
    
    submit = st.form_submit_button("GENERATE SOCIAL PROFILE")

# 4. Results Logic
if submit:
    score = sum(checks)
    percentage = int((score / 10) * 100)
    
    with st.status("Accessing Sociological Databases...", expanded=True) as status:
        time.sleep(1)
        st.write("Cross-referencing Durkheim's theories...")
        time.sleep(1)
        status.update(label="Analysis Complete!", state="complete", expanded=False)

    st.divider()
    
    # Visual Percentage Result
    st.header(f"Your Conformity Level: {percentage}%")
    st.progress(percentage / 100)
    
    if percentage <= 30:
        st.error("### RESULT: SYSTEM GLITCH")
        st.write("You are a **Sociology Rebel**. You have successfully resisted the 'Personality Factory.' Your individuality remains unformatted by the machine.")
    elif percentage <= 70:
        st.warning("### RESULT: STANDARD PRODUCT")
        st.write("You are **Successfully Socialized**. You fit the 'Society in Miniature' perfectly. A balanced participant in the social contract.")
    else:
        st.success("### RESULT: ELITE AGENT")
        st.write("You ARE the system. Parsons and Durkheim would be proud. You don't just follow social norms—you embody them.")

    st.balloons()
