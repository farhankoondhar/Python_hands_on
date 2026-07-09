import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import json
import os
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="MoodMapper",
    page_icon="🌊",
    layout="centered",
    initial_sidebar_state="expanded"
)

class MoodDatabase:
    def __init__(self):
        self.data_dir = Path("data")
        self.data_dir.mkdir(exist_ok=True)
        self.data_file = self.data_file = self.data_dir / "mood_entries.json"
        self.load_data()
    
    def load_data(self):
        if self.data_file.exists():
            try:
                with open(self.data_file, 'r') as f:
                    self.entries = json.load(f)
            except (json.JSONDecodeError, Exception):
                self.entries = []
        else:
            self.entries = []
    
    def save_data(self):
        with open(self.data_file, 'w') as f:
            json.dump(self.entries, f, indent=2)
    
    def add_entry(self, emotion, note, intensity=5):
        entry = {
            'id': len(self.entries) + 1,
            'timestamp': datetime.now().isoformat(),
            'emotion': emotion,
            'note': note,
            'intensity': intensity,
            'date': datetime.now().strftime("%Y-%m-%d")
        }
        self.entries.append(entry)
        self.save_data()
        return entry
    
    def get_recent_entries(self, limit=10):
        return sorted(self.entries, key=lambda x: x['timestamp'], reverse=True)[:limit]
    
    def get_emotion_stats(self):
        if not self.entries:
            return pd.DataFrame()
        return pd.DataFrame(self.entries)

def apply_custom_styles():
    st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .emotion-btn { border-radius: 10px; padding: 1rem; margin: 0.3rem; }
    .main-header { text-align: center; color: #2E86AB; margin-bottom: 2rem; }
    .mood-card { background: white; padding: 1rem; border-radius: 10px; margin: 0.5rem 0; }
    </style>
    """, unsafe_allow_html=True)

def main():
    # Initialize database
    db = MoodDatabase()
    apply_custom_styles()
    
    # Sidebar
    with st.sidebar:
        st.title("🌊 Navigation")
        st.markdown("---")
        if db.entries:
            st.metric("Total Entries", len(db.entries))
            st.metric("Days Tracked", len(set(entry['date'] for entry in db.entries)))
    
    # Main content
    st.markdown('<div class="main-header">', unsafe_allow_html=True)
    st.title("🌊 MoodMapper")
    st.caption("Track Your Emotional Journey")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Emotion selection
    emotions = {
        "😊 Happy": "happy",
        "😢 Sad": "sad", 
        "😴 Tired": "tired",
        "⚡ Energetic": "energetic",
        "😌 Calm": "calm",
        "😠 Angry": "angry",
        "😨 Anxious": "anxious",
        "😃 Excited": "exciting"
    }
    
    st.subheader("How are you feeling right now?")
    cols = st.columns(4)
    selected_emotion = None
    selected_emotion_display = None
    
    for i, (emotion_display, emotion_value) in enumerate(emotions.items()):
        with cols[i % 4]:
            if st.button(emotion_display, key=emotion_value, use_container_width=True):
                selected_emotion = emotion_value
                selected_emotion_display = emotion_display
    
    # Emotion details
    if selected_emotion:
        st.markdown("---")
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.subheader("Selected Mood")
            st.markdown(f"# {selected_emotion_display}")
        
        with col2:
            note = st.text_area("Add context (optional):", placeholder="What's on your mind?")
            intensity = st.slider("Intensity:", 1, 10, 5)
            
            if st.button("💾 Save Entry", type="primary"):
                db.add_entry(selected_emotion, note, intensity)
                st.success("Mood saved! 🌟")
                st.balloons()
    
    # Insights
    if db.entries:
        st.markdown("---")
        st.subheader("📊 Your Emotional Insights")
        
        df = db.get_emotion_stats()
        emotion_counts = df['emotion'].value_counts()
        
        if not emotion_counts.empty:
            fig, ax = plt.subplots(figsize=(10, 4))
            emotion_counts.plot(kind='bar', ax=ax, color='skyblue')
            ax.set_title('Your Emotional Patterns')
            ax.set_ylabel('Number of Entries')
            plt.xticks(rotation=45)
            st.pyplot(fig)
            plt.close(fig)
        
        # Recent entries
        st.write("**Recent Entries**")
        for entry in db.get_recent_entries(5):
            col1, col2 = st.columns([1, 4])
            with col1:
                st.write(f"**{entry['emotion'].title()}**")
            with col2:
                st.write(entry['note'] if entry['note'] else "*No note*")
            st.divider()

if __name__ == "__main__":
    main()