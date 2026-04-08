import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(page_title="Social Breakdown Quiz", page_icon="🧪")

st.markdown("""
    <style>
    .main-title { color: #ad1457; text-align: center; font-size: 45px; font-weight: bold; }
    .quiz-box { background-color: #fce4ec; padding: 20px; border-radius: 15px; border: 2px solid #ad1457; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="main-title">SOCIAL BREAKDOWN QUIZ</div>', unsafe_allow_html=True)
st.write("<center><i>Are you a Sociology Rebel or a Perfectly Molded Product?</i></center>", unsafe_allow_html=True)
st.divider()

# 2. The Questions
items = [
    "Do you use a different 'voice' at home versus in public?",
    "Have you ever accidentally called a teacher 'Mom' or 'Dad'?",
    "Do you feel a spike of anxiety when you hear a school bell or timer?",
    "Have you ever hidden in a store to avoid seeing a professor?",
    "Did you grow up with toys strictly 'meant' for your gender?",
    "Do you feel your self-worth is tied to your GPA or grades?",
    "Have you ever raised your hand to speak while at the dinner table?",
    "Does your family have 'unspoken rules' that outsiders wouldn't get?",
    "Do you feel intense guilt even if you are only 2 minutes late?"
]

# 3. Quiz Form
with st.form("bingo_quiz"):
    st.write("### Select all that apply to you:")
    
    # We use a dictionary to store responses
    responses = {}
    
    # Split questions into two columns for better flow
    col1, col2 = st.columns(2)
    
    for i, question in enumerate(items):
        if i % 2 == 0:
            responses[i] = col1.checkbox(question)
        else:
            responses[i] = col2.checkbox(question)
            
    submit = st.form_submit_button("SUBMIT FOR ANALYSIS")

# 4. Processing Results
if submit:
    score = sum(responses.values())
    
    with st.status("Running Sociological Algorithms...", expanded=True) as status:
        st.write("Scanning for internalized norms...")
        time.sleep(1)
        st.write("Evaluating peer-group influence...")
        time.sleep(1)
        st.write("Comparing data for Nour & Houda...")
        time.sleep(1)
        status.update(label="Analysis Complete!", state="complete", expanded=False)

    st.divider()
    
    # Final Result Display
    st.balloons()
    st.markdown(f"## YOUR CONFORMITY SCORE: **{score}/9**")

    if score <= 3:
        st.error("### RESULT: SYSTEM GLITCH DETECTED.")
        st.write("**Diagnosis:** You are a **Sociology Rebel**. You have successfully resisted the 'Personality Factory.' Your individuality remains unformatted by the machine.")
    elif score <= 6:
        st.warning("### RESULT: STANDARD PRODUCT APPROVED.")
        st.write("**Diagnosis:** You are **Successfully Socialized**. You fit the 'Society in Miniature' perfectly. A balanced participant in the social contract.")
    else:
        st.success("### RESULT: ELITE AGENT OF CONFORMITY.")
        st.write("**Diagnosis:** **The Ultimate Social Subject.** Parsons and Durkheim would be proud. You don't just follow the system—you ARE the system!")
   
        
        
