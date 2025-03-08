import streamlit as st
import random

# Growth Mindset Tips & Challenges
growth_tips = [
    "View challenges as opportunities to grow.",
    "Embrace mistakes as a chance to learn.",
    "Stay persistent even when things get tough.",
    "Celebrate effort, not just results.",
    "Be curious and open to new learning experiences."
]

growth_challenges = [
    "Write down one mistake you made recently and what you learned from it.",
    "Try learning a new skill for 10 minutes today.",
    "Ask for feedback on something you're working on.",
    "Encourage someone else to keep going despite difficulties.",
    "Reflect on a past challenge you overcame. What did you learn?"
]

# Random Motivation Quotes
motivational_quotes = [
    "“Success is not final, failure is not fatal: it is the courage to continue that counts.” – Winston Churchill",
    "“The only limit to our realization of tomorrow is our doubts of today.” – Franklin D. Roosevelt",
    "“Do not be embarrassed by your failures, learn from them and start again.” – Richard Branson",
    "“Growth and comfort do not coexist.” – Ginni Rometty",
    "“It does not matter how slowly you go as long as you do not stop.” – Confucius"
]

# Streamlit UI
st.title("🚀 Growth Mindset Challenge")

st.subheader("What is a Growth Mindset?")
st.write("""
A **growth mindset** is the belief that abilities can be developed through hard work, perseverance, and learning from mistakes.  
Embrace challenges, seek feedback, and stay curious!  
""")

# Display a random tip
st.subheader("💡 Growth Mindset Tip")
st.info(random.choice(growth_tips))

# Display a random challenge
st.subheader("🎯 Today's Challenge")
st.warning(random.choice(growth_challenges))

# User Reflection
st.subheader("📝 Reflection")
reflection = st.text_area("What did you learn from today's challenge?")
if st.button("Submit"):
    if reflection:
        st.success("Great! Reflection is a key part of growth. Keep going! 💪")
    else:
        st.error("Please enter your reflection to proceed.")

# Motivation Section
st.subheader("🔥 Stay Motivated!")
st.write(random.choice(motivational_quotes))
