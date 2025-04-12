import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_drawable_canvas import st_canvas

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Mind-z", layout="wide")

# ---- STYLING ----
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(to right, #f3e8ff, #e5d4ff);
        }
    </style>
""", unsafe_allow_html=True)

# ---- SIDEBAR NAVIGATION ----
with st.sidebar:
    selected = option_menu(
        menu_title="Mind-z 🧠",
        options=["Home", "CBT", "Yoga", "Tai Chi", "Qigong", "Journal", "Notepad", "Art Therapy"],
        icons=["house", "clipboard-check", "sunrise", "activity", "wind", "journal", "pencil-square", "paintbrush"],
        menu_icon="heart",
        default_index=0,
    )

# ---- PAGE LOGIC ----
if selected == "Home":
    st.title("Welcome to Mind-z 🌿")
    st.subheader("Your pocket friendly therapy hub.")
    
    st.markdown("### How are you feeling today?")
    feeling = st.selectbox("Choose an emotion:", ["Happiness", "Sadness", "Anger", "Fear", "Surprise", "Disgust"])
    therapy_choice = st.selectbox("What kind of therapy would you like?", ["Select", "CBT", "Yoga", "Tai Chi", "Qigong", "Art Therapy"])

    if therapy_choice != "Select":
    st.success(f"Redirecting to **{therapy_choice}** for managing **{feeling.lower()}**.")
    st.rerun()

elif selected == "CBT":
    st.subheader("🧠 CBT Exercises")
    st.markdown("[📘 Go to CBT Guide](https://youtu.be/8-2WQF3SWwo?feature=shared)")

elif selected == "Yoga":
    st.subheader("🧘‍♀️ Yoga Practice")
    st.markdown("[🧘 Visit Yoga Journal](https://youtu.be/8TuRYV71Rgo?feature=shared)")

elif selected == "Tai Chi":
    st.subheader("🌬 Tai Chi Sessions")
    st.markdown("[🌿 Tai Chi for Health Institute](https://youtu.be/MGGfpA6XuBs?feature=shared/)")

elif selected == "Qigong":
    st.subheader("💫 Qigong Energy Work")
    st.markdown("[💫 Learn Qigong](https://youtu.be/7KTXgggIdZ4?feature=shared/)")

elif selected == "Journal":
    st.subheader("📝 Your Private Journal")
    journal_entry = st.text_area("Write about your day or feelings:")
    if st.button("Save Entry"):
        with open("journal.txt", "a", encoding="utf-8") as f:
            f.write(journal_entry + "\n\n")
        st.success("✅ Journal entry saved!")

elif selected == "Notepad":
    st.subheader("🗒️ Notepad")
    note = st.text_area("Write your notes:")
    if st.button("Save Note"):
        with open("notes.txt", "a", encoding="utf-8") as f:
            f.write(note + "\n\n")
        st.success("✅ Note saved!")

elif selected == "Art Therapy":
    st.subheader("🎨 Art Therapy Canvas")
    st.markdown("**Instructions:** Paint how you're feeling or a happy memory. Let your emotions flow. 🌈")

    stroke_width = st.slider("🖌️ Brush Size:", 1, 25, 5)
    stroke_color = st.color_picker("🎨 Brush Color:", "#000000")
    bg_color = st.color_picker("🌈 Canvas Background:", "#ffffff")
    drawing_mode = st.selectbox("✏️ Drawing Tool:", ("freedraw", "line", "rect", "circle", "transform"))
    eraser_mode = st.checkbox("Use Eraser")

    if eraser_mode:
        stroke_color = bg_color  # acts like eraser

    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color=bg_color,
        height=400,
        drawing_mode=drawing_mode,
        key="canvas",
    )
