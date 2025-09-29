import streamlit as st
import google.generativeai as genai
import random

# Set up Gemini API Key securely
API_KEY =st.secrets["GOOGLE_API_KEY"] 
genai.configure(api_key=API_KEY)

# Spiritual paragraphs
spiritual_sources = {
    "Bhagavad Gita": "Chapter 2, Verse 47: Your right is to perform your duty only, but never to its fruits...",
    "Quran": "Surah Al-Baqarah, Verse 286: Allah does not burden a soul beyond that it can bear...",
    "Bible": "Philippians 4:13: I can do all things through Christ who strengthens me...",
    "Guru Granth Sahib": "Ang 10: Recognize the Divine Light within all...",
    "Tripitaka": "Dhammapada, Verse 183: Do no harm, cultivate good, purify your mind..."
}

# Motivational quotes database
motivational_quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Do what you can, with what you have, where you are. - Theodore Roosevelt",
    "Act as if what you do makes a difference. It does. - William James",
    "Be kind, for everyone you meet is fighting a hard battle. - Plato",
    "What you think, you become. What you feel, you attract. - Buddha",
    "You do not rise to the level of your goals. You fall to the level of your systems. - James Clear (Atomic Habits)",
    "If you want to be happy, set a goal that commands your thoughts... - Napoleon Hill (Think and Grow Rich)",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Opportunities don't happen. You create them. - Chris Grosser",
    "Your time is limited, so don’t waste it living someone else’s life. - Steve Jobs"
]


# Function to fetch AI-generated advice
def get_advice(age_group, concern):
    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = f"""
    Provide holistic mental well-being advice for a {age_group} individual facing '{concern}'.
     **🔍 EMOTIONAL INTELLIGENCE ANALYSIS OF THE CONCERN**  
    - What underlying emotions (fear, anxiety, self-doubt, stress) might the user be experiencing?  
    - Apply Daniel Goleman’s Emotional Intelligence framework to analyze this.  
    - Suggest an **emotion-labeling exercise** (from *Atlas of the Heart* by Brené Brown).  
    
     **📜 SPIRITUAL PERSPECTIVE (WITH SOURCES)**  
    - Extract wisdom from each and display in different lines:  
      - **Bhagavad Gita** (cite exact verse)  
      - **Quran** (cite Surah and Ayah)  
      - **Bible** (cite Book, Chapter, and Verse)  
      - **Guru Granth Sahib** (cite Ang number)  
      - **Tripitaka** (cite text and verse)  
    
    **🧠 PSYCHOLOGY & PHILOSOPHICAL REFRAMING OF '{concern.upper()}'**  
    - Use **Stoicism (Marcus Aurelius, Seneca, Epictetus)** to suggest a resilient mindset.  
    - Apply **Existentialism (Nietzsche, Sartre, Viktor Frankl)** to explore meaning.  
    - Use **Positive Psychology (Martin Seligman, Mihaly Csikszentmihalyi)** to shift perspectives. 
    
    **🧘 MINDFULNESS & MEDITATION TIPS **
       - Share a mindfulness or meditation technique related to '{concern}'

    **🔄 DAILY HABIT SUGGESTIONS **   
       - Recommend 3 small, easy-to-follow habits that build mental resilience related to '{concern}'.

    **🔬 SCIENTIFIC EXPLANATION OF EMOTIONS**   
       - Explain why the user might be feeling this way from a neuroscience perspective related to '{concern}'.

    **🧠 COGNITIVE REFRAMING TECHNIQUES**  
       - Suggest Cognitive Behavioral Therapy (CBT) techniques to shift negative thinking patterns related to '{concern}'.

    **🍏 PHYSICAL HEALTH & DIET ADVICE**  
       - Provide dietary or physical activity suggestions to boost mood and energy related to '{concern}'.

    **🎵 MUSIC & ART THERAPY RECOMMENDATIONS**  
       - Recommend soothing music genres with 3 songs with the artist name, art activities, or creative outlets for stress relief related to '{concern}'.

    **🔬 SCIENTIFIC EXPLANATION OF EMOTIONS**  
       - Create a short, comforting story or analogy that aligns with the user's concern in 200 words related to '{concern}'

    **📚 PSYCHOLOGICAL TIPS FROM SELF-DEVELOPMENT BOOKS & EXPERTS**  
       - Quote 1 insight from one of these **James Clear, Eckhart Tolle, Carol Dweck, Stephen Covey, and David Goggins** 
       - Extract 1 insight from one of these *Atomic Habits*, *Dare to Lead*, *The Power of Now*, and others 
       - Provide 1 actionable tip based on their teachings.
       
    **💡 RELEVANT MOTIVATIONAL & SPIRITUAL QUOTES**  
       - Generate 2 motivational and 2 spiritual quotes related to '{concern}'.  
       - These should be in the style of great thinkers like Steve Jobs, Winston Churchill, and Marcus Aurelius.   

    **📚 RECOMMENDED READINGS FOR DEEPER INSIGHTS**  
       - List at 2 **books** and 2 **articles** that can help the user gain a deeper understanding of mental well-being.  

    Ensure that the response is **empathetic, scientifically sound, and actionable**.
    """

    response = model.generate_content(prompt)
    return response.text if response else "Sorry, no advice available now."


# Function to fetch YouTube video recommendation
def get_youtube_link(age_group, concern):
    query = f"{age_group} mental health advice for {concern}"
    return f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"


# Streamlit UI Setup
st.set_page_config(page_title="Mental Health & Self-Improvement", layout="wide")
st.markdown("<h1 class='main-title'>🌿 Mental Health & Self-Improvement App</h1>", unsafe_allow_html=True)
st.image("https://img.freepik.com/free-vector/mental-health-logo_23-2148476181.jpg", width=100)
st.header("🧘‍♂️ USER INPUT")

# User Inputs
age_group = st.selectbox("Select Your Age Group:",
                                 ["Child", "Teenager", "Young Adult", "Middle-aged", "Senior"])
concern = st.text_area("Describe Your Concern or Challenge:")

if st.button("Get Advice"):
    if concern:
        st.subheader("📜 Personalized Advice:")
        st.write(get_advice(age_group, concern))

        st.markdown("---")
        st.subheader("💡 Inspirational Quotes:")
        random_quotes = random.sample(motivational_quotes, 3)  # Pick 3 random quotes
        for quote in random_quotes:
            st.write(f"*{quote}*")

        st.markdown("---")
        st.subheader("🎥 Recommended YouTube Video:")
        st.markdown(f"[Click here to watch]({get_youtube_link(age_group, concern)})")

        st.markdown("---")
        st.subheader("📖 Spiritual Insights for self development:")
        for source, paragraph in spiritual_sources.items():
            st.write(f"**{source}**: *{paragraph}*")


    else:
        st.warning("⚠️ Please enter a concern to receive advice.")





