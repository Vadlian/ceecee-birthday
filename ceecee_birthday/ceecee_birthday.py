import streamlit as st
import random
import os

# Get the exact folder where this script is saved
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Page Configuration
st.set_page_config(
    page_title="For CeeCee Only ✨",
    page_icon="🔒",
    layout="centered"
)

# Custom Styling
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0d0f12 0%, #1a1d24 100%);
        color: #f1f5f9;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    .main-title {
        font-size: 2.8rem;
        font-weight: 800;
        text-align: center;
        background: linear-gradient(120deg, #f39c12, #f1c40f, #e67e22);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }
    .sub-title {
        text-align: center;
        color: #94a3b8;
        font-size: 1.1rem;
        margin-bottom: 25px;
    }
    .custom-card {
        background: rgba(30, 41, 59, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 24px;
        backdrop-filter: blur(10px);
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.4);
        margin-bottom: 25px;
        text-align: center;
    }
    .stButton > button {
        background: linear-gradient(135deg, #d35400 0%, #e67e22 100%) !important;
        color: #ffffff !important;
        font-weight: 700 !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 12px 24px !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- PRIVACY LOCK SCREEN ---
# Change "ceecee2026" to whatever secret password or date you want her to type!
SECRET_PASSWORD = "ceecee" 

st.markdown("<h1 class='main-title'>🔒 Private Access</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>This page is locked. Enter the secret code to proceed.</p>", unsafe_allow_html=True)

st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
entered_password = st.text_input("Enter Secret Password:", type="password")
st.markdown("</div>", unsafe_allow_html=True)

# Check if password matches
if entered_password == SECRET_PASSWORD:
    st.success("Access Granted! Enjoy your day ✨")
    st.balloons()

    # --- ALL YOUR MAIN APP CONTENT STARTS HERE ---
    st.markdown("<h1 class='main-title'>✨ Happy Birthday, CeeCee ✨</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>Today is all about celebrating YOU 👑</p>", unsafe_allow_html=True)

    # Music Player Section
    music_path = os.path.join(BASE_DIR, "music", "bg_music.mp3")
    if os.path.exists(music_path):
        st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
        st.markdown("### 🎵 Press Play for Her Soundtrack")
        with open(music_path, "rb") as audio_file:
            st.audio(audio_file.read(), format="audio/mp3")
        st.markdown("</div>", unsafe_allow_html=True)

    # Main Spotlight Cover Photo
    st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
    cover_path = os.path.join(BASE_DIR, "photos", "main_photo.jpg")
    if os.path.exists(cover_path):
        st.image(cover_path, caption="The Main Attraction ⭐", use_container_width=True)
    else:
        st.info("💡 Place `main_photo.jpg` inside the `photos/` folder!")

    st.markdown("### Happy Birthday to a Pure Gem ✨")
    st.write("I created this exclusive page just for you. Hope this year brings you everything you've been working for and more!")
    st.markdown("</div>", unsafe_allow_html=True)

    # Photo Gallery
    st.markdown("## 📸 CeeCee's Gallery")
    st.write("Just a reminder of how effortlessly stunning you are:")

    col1, col2 = st.columns(2)
    with col1:
        m1_path = os.path.join(BASE_DIR, "photos", "memory1.jpg")
        if os.path.exists(m1_path):
            st.image(m1_path, use_container_width=True)
            st.caption("Pure Elegance ✨")

        m2_path = os.path.join(BASE_DIR, "photos", "memory2.jpg")
        if os.path.exists(m2_path):
            st.image(m2_path, use_container_width=True)
            st.caption("Unmatched Energy 🔥")

    with col2:
        m3_path = os.path.join(BASE_DIR, "photos", "memory3.jpg")
        if os.path.exists(m3_path):
            st.image(m3_path, use_container_width=True)
            st.caption("Main Character Energy 🌟")

        st.markdown("<div style='padding: 15px; background: rgba(255,255,255,0.03); border-radius: 12px; border: 1px solid rgba(255,255,255,0.05); text-align: center; margin-top: 10px;'>", unsafe_allow_html=True)
        st.write("👑 **Queen of the Day**")
        st.caption("Looking forward to taking a million more photos together!")
        st.markdown("</div>", unsafe_allow_html=True)

    st.write("---")

    # Compliment Generator
    st.markdown("## 💌 A Few Things You Should Know")
    compliments = [
        "Your ambition and drive are genuinely inspiring.",
        "You have a natural confidence and elegance that lights up any room.",
        "Your laughter is easily the best sound in the world.",
        "You have a heart of gold and a rare, genuine soul.",
        "You make everything around you look cooler and better.",
        "You deserve every single good thing coming your way this year!"
    ]

    if st.button("Click for a Birthday Note 💬", use_container_width=True):
        chosen_compliment = random.choice(compliments)
        st.balloons()
        st.success(f"**{chosen_compliment}**")

    st.write("---")

    # Fireworks Finale
    st.markdown("## 🎁 Birthday Grand Finale")
    if st.button("Launch Fireworks! 🎆", use_container_width=True):
        st.snow()
        st.balloons()
        st.toast("BOOM! Happy Birthday CeeCee! 🎆🎂", icon="👑")

        import streamlit.components.v1 as components
        fireworks_html = """
        <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
        <script>
            var duration = 3.5 * 1000;
            var animationEnd = Date.now() + duration;
            var defaults = { startVelocity: 30, spread: 360, ticks: 60, zIndex: 9999 };
            function randomInRange(min, max) { return Math.random() * (max - min) + min; }
            var interval = setInterval(function() {
              var timeLeft = animationEnd - Date.now();
              if (timeLeft <= 0) { return clearInterval(interval); }
              var particleCount = 50 * (timeLeft / duration);
              confetti(Object.assign({}, defaults, { particleCount, origin: { x: randomInRange(0.1, 0.3), y: Math.random() - 0.2 } }));
              confetti(Object.assign({}, defaults, { particleCount, origin: { x: randomInRange(0.7, 0.9), y: Math.random() - 0.2 } }));
            }, 250);
        </script>
        """
        components.html(fireworks_html, height=50)
        st.markdown("### 🥂 Cheers to another year of health, wealth, success, and pure joy!")

elif entered_password != "":
    st.error("Incorrect password! Try again.")
