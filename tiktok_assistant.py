import streamlit as st
from datetime import datetime
import random

# Mock trending hashtags and creators
trending_hashtags = [
    "#TocaBoca", "#TocaLifeWorld", "#TocaBuilds", "#CozyToca", "#TocaDecor", "#TocaRoutine"
]

suggested_creators = [
    "@TocaDreams", "@TocaBuilderGirl", "@DailyToca", "@TocaAesthetic", "@TocaLifeVibes"
]

sample_comments = [
    "Love this build! So cozy and creative 💛",
    "The color palette is amazing 😍",
    "I never thought to decorate it like that! Inspo ✨",
    "This gives such chill vibes, love it! 🌊",
    "So satisfying to watch 👏 #TocaGoals"
]

# App title
st.title("🌟 Toca TikTok Growth Assistant")
st.write("Your daily helper for growing a cozy Toca Boca TikTok account.")

# Section 1: Trending Hashtags
st.header("🔥 Today's Trending Hashtags")
st.write(", ".join(random.sample(trending_hashtags, 4)))

# Section 2: Creators to Follow
st.header("🤝 Creators You Should Follow Today")
st.write("Here are 3 Toca creators to check out and engage with:")
st.write(random.sample(suggested_creators, 3))

# Section 3: Comment Suggestions
st.header("💬 Comments to Leave on Trending Videos")
st.write("Pick 2–3 of these to leave thoughtful comments today:")
st.write(random.sample(sample_comments, 3))

# Section 4: Content Idea Generator
st.header("🎥 Content Idea for Tomorrow")
st.write("Try creating a short around:")
content_ideas = [
    "Aesthetic bathroom makeover in the Neon Apartments",
    "Toca-style morning routine with beach vibes",
    "3 tips for organizing your Toca home",
    "Before and after: transforming the smallest room",
    "Matching outfits with your Toca characters!"
]
st.write(random.choice(content_ideas))

# Footer
st.markdown("---")
st.caption(f"Generated on {datetime.now().strftime('%B %d, %Y')} | Sagashi's Assistant")
