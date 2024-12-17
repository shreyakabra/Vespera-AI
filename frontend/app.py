import streamlit as st
import requests

# Backend Flask server URL
BACKEND_URL = "http://127.0.0.1:5000"

# App title and sidebar
st.set_page_config(page_title="Vespera AI Storytelling", layout="wide")
st.title("Vespera AI Storytelling App")
st.sidebar.title("Navigation")
st.sidebar.write("Explore the app to generate, save, or view stories.")

# Input form for story generation
st.header("Generate a Story")
prompt = st.text_area("Enter your story prompt:", placeholder="Once upon a time...")
mode = st.selectbox("Choose a storytelling mode:", ["fantasy", "sci-fi", "mystery", "general"])
max_length = st.slider("Set maximum story length (tokens):", min_value=50, max_value=2000, value=300)
temperature = st.slider("Set creativity level (temperature):", min_value=0.1, max_value=1.5, value=0.7)

# Session state for story persistence
if "generated_story" not in st.session_state:
    st.session_state.generated_story = None

# Generate a story
if st.button("Generate Story"):
    if prompt.strip():
        with st.spinner("Generating your story..."):
            try:
                response = requests.post(
                    f"{BACKEND_URL}/generate_story",
                    json={
                        "prompt": prompt,
                        "max_length": max_length,
                        "temperature": temperature,
                        "mode": mode
                    }
                )
                if response.status_code == 200:
                    story = response.json().get("stories", ["No story generated."])[0]  # Get the first story
                    st.session_state.generated_story = story
                    st.subheader("Generated Story:")
                    st.write(story)
                else:
                    st.error(f"Failed to generate story. Error: {response.text}")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
    else:
        st.error("Please enter a valid prompt!")

st.markdown("---")

# View saved stories
st.header("View Saved Stories")
if st.button("View Saved Stories"):
    with st.spinner("Fetching saved stories..."):
        try:
            response = requests.get(f"{BACKEND_URL}/get_stories")
            if response.status_code == 200:
                saved_stories = response.json().get("stories", [])
                if saved_stories:
                    for idx, story in enumerate(saved_stories, start=1):
                        st.markdown(f"### Story {idx}")
                        st.markdown(f"**Prompt:** {story['prompt']}")
                        st.write(story['story'])
                        st.markdown("---")
                else:
                    st.info("No saved stories found.")
            else:
                st.error(f"Failed to fetch stories. Error: {response.text}")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

st.markdown("---")

# Save the generated story
st.header("Save the Generated Story")
if st.session_state.generated_story:
    if st.button("Save Story"):
        with st.spinner("Saving your story..."):
            try:
                save_data = {"prompt": prompt, "story": st.session_state.generated_story}
                response = requests.post(f"{BACKEND_URL}/save_story", json=save_data)
                if response.status_code == 200:
                    st.success("Story saved successfully!")
                    st.session_state.generated_story = None  # Clear saved story after saving
                else:
                    st.error(f"Failed to save story. Error: {response.text}")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
else:
    st.info("Generate a story first to save!")

st.markdown("---")
