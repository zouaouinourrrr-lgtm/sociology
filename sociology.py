import streamlit as st

# 1. Page Setup
st.set_page_config(page_title="Social Breakdown Bingo", page_icon="🎲")

# 2. Styling the Header
st.markdown("""
    <style>
    .title {
        color: #ad1457;
        text-align: center;
        font-size: 40px;
        font-weight: bold;
    }
    .subtitle {
        text-align: center;
        font-style: italic;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="title">SOCIAL BREAKDOWN BINGO</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Are you a Sociology Rebel or a Perfectly Molded Product?</div>', unsafe_allow_html=True)

# 3. The Bingo Items
items = [
    "Home Voice vs Public Voice", "Called teacher 'Mom'", "Bell Anxiety",
    "Hidden from prof at mall", "Gendered Toys", "Grade Chaser",
    "Hand Raising at home", "Secret Family Rules", "Guilt for being late"
]

# 4. Creating the 3x3 Grid
# We use columns to make it look like a bingo card
cols = st.columns(3)
checkbox_states = []

for i, item in enumerate(items):
    with cols[i % 3]:
        # This creates the checkbox and saves its True/False value
        is_checked = st.checkbox(item, key=f"check_{i}")
        checkbox_states.append(is_checked)

st.markdown("---")

# 5. The Diagnosis Logic
# Center the button using columns
left, mid, right = st.columns([1, 2, 1])

with mid:
    if st.button("GET DIAGNOSIS", use_container_width=True):
        score = sum(checkbox_states)
        
        st.subheader("--- ANALYZING DATA FOR NOUR & HOUDA ---")
        st.metric("CONFORMITY SCORE", f"{score}/9")
        
        if score <= 3:
            st.error("RESULT: SYSTEM GLITCH DETECTED.")
            st.write("**Diagnosis:** You have resisted the Personality Factory. A true sociology rebel!")
        elif score <= 6:
            st.warning("RESULT: STANDARD PRODUCT APPROVED.")
            st.write("**Diagnosis:** Successfully socialized. You fit the 'Society in
