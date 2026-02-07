import streamlit as st
import pickle
import re
import nltk
import time
import sklearn
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# --- PAGE CONFIG ---
st.set_page_config(page_title="CyberGuard AI", page_icon="🛡️", layout="centered")

# --- CUSTOM CSS FOR BEAUTIFICATION ---
st.markdown("""
    <style>
    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #c0c0aa 0% ,#1cefff 20%, #9cecfb 40%, #65c7f7 60%, #0052d4 100%);
    }
    .stSidebar {
        width: 300px !important;
    }
    /* Title styling */
    .main-title {
        font-size: 3rem;
        font-weight: 800;
        color: #000000;
        text-align: center;
        margin-bottom: 0px;
    }
    
    .ai{
        color: #1E3A8A !important;    
    }
            
    p {
        font-weight: 600 !important; /* Specific heavy weight */
    }
    
    /* Subtitle styling */
    .sub-title {
        font-size: 1.1rem;
        color: #4B5563;
        text-align: center;
        margin-bottom: 2rem;
    }

    /* Glassmorphism Card for input */
    .input-card {
        background: rgba(255, 255, 255, 0.7);
        border-radius: 15px;
        padding: 25px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# --- SETUP & ASSETS ---

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

with open('main_textproject1.pkl', 'rb') as f:
    dec = pickle.load(f)
with open('vect.pkl', 'rb') as f:
    sc = pickle.load(f)

stop_words = set(stopwords.words('english'))
lem = WordNetLemmatizer()

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2092/2092663.png", width=100)
    st.title("About CyberGuard")
    st.info("Using Machine Learning to detect: \n* Gender Harassment\n* Religion/Ethinicity Hate\n* Race Bullying")
    st.divider()
    st.markdown("Developed by: PAVAN SAI K")

# --- MAIN UI ---
st.markdown("<h1 class='main-title'>🛡️ CyberGuard <span class ='ai'>AI</span></h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Advanced Toxic Content Detection for Safer Digital Spaces</p>", unsafe_allow_html=True)

# Wrapping input in a stylized container
with st.container():
    te = st.text_area("Analyze Text / Social Media Post:", placeholder="Paste content here...", height=150)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        scan_btn = st.button("🔍 SCAN CONTENT", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

def clean(text):
    data = re.findall('[a-zA-Z]{1,15}', text.lower())
    words = [lem.lemmatize(i) for i in data if i not in stop_words]
    return ' '.join(words)

st.markdown("<br>", unsafe_allow_html=True)

# --- LOGIC ---
if scan_btn:
    if te.strip() == "":
        st.toast("⚠️ Please enter some text first!", icon="🚨")
    else:
        # 1. Processing
        text = clean(te)
        
        # 2. Scanning Animation
        with st.status("🚀 Initializing Neural Scan...", expanded=True) as status:
            st.write("Cleaning linguistic noise...")
            time.sleep(0.6)
            st.write("Vectorizing input tokens...")
            input_df = sc.transform([text])
            time.sleep(0.6)
            st.write("Predicting toxicity probability...")
            result = dec.predict(input_df)[0]
            status.update(label="Analysis Complete!", state="complete", expanded=False)

        # 3. Dynamic Results Display
        st.divider()
        
        if result == "not_cyberbullying":
            cols = st.columns(2)
            cols[0].metric("Safety Rating", "100%", "Clean")
            cols[1].metric("Threat Level", "None", "-0%")
            st.success(f"### ✅ Content is Safe \n No toxic patterns detected in: *\"{text}\"*")
        else:
            st.error(f"### 🚨 Toxic Content Detected")
            st.warning(f"**Classification:** {result.upper()}")
            
            # Recommendation box
            with st.expander("🛡️ Safety Recommendations"):
                st.write("""
                1. **Restrict:** Consider blocking the user.
                2. **Report:** Use the platform's reporting tools.
                3. **Ignore:** Avoid engaging with high-toxicity content.

                """)

