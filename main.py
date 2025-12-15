import streamlit as st

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="ScreenerPro – Test Layout",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =====================================================
# GLOBAL STYLES (HEADER + FOOTER SAFE)
# =====================================================
st.markdown("""
<style>
body {
    background-color: #f8fafc;
    font-family: Inter, sans-serif;
}

/* FOOTER */
.footer {
    background: #1e3a8a;
    padding: 60px 40px;
    color: #e2e8f0;
    margin-top: 80px;
}

.footer-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 40px;
    max-width: 1200px;
    margin: auto;
}

.footer h4 {
    color: #38bdf8;
    margin-bottom: 16px;
}

.footer a {
    color: #94a3b8;
    display: block;
    margin-bottom: 10px;
    text-decoration: none;
}

.footer a:hover {
    color: #38bdf8;
}

.footer-bottom {
    margin-top: 40px;
    border-top: 1px solid #3b82f6;
    padding-top: 20px;
    text-align: center;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# MAIN CONTENT (SIMULATING main.py APP CONTENT)
# =====================================================
st.title("🧪 ScreenerPro – Main App Test Page")

st.write("""
This is a **test main.py** to verify:
- Footer visibility
- Footer position
- No black / white screen bug
- Works even when page is scrolled
""")

for i in range(25):
    st.write(f"Dummy content line {i+1} to enable scrolling...")

# =====================================================
# FOOTER (SAME AS LANDING PAGE DESIGN)
# =====================================================
st.markdown("""
<div class="footer">
    <div class="footer-grid">
        <div>
            <h4>ScreenerPro</h4>
            <a href="#">About Us</a>
            <a href="#">Careers</a>
            <a href="#">Privacy Policy</a>
        </div>

        <div>
            <h4>Solutions</h4>
            <a href="#">Recruiter Platform</a>
            <a href="#">Candidate Tools</a>
            <a href="#">AI Workflow</a>
        </div>

        <div>
            <h4>Resources</h4>
            <a href="#">Download Proposal</a>
            <a href="#">Request Support</a>
        </div>

        <div>
            <h4>Connect</h4>
            <a href="#">LinkedIn</a>
            <a href="#">Email Us</a>
        </div>
    </div>

    <div class="footer-bottom">
        © 2025 ScreenerPro Technologies Inc. – AI Talent Intelligence Platform
    </div>
</div>
""", unsafe_allow_html=True)
