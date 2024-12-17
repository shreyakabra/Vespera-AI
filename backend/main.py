from flask import Flask, request, jsonify
from g4f.client import Client
from pymongo import MongoClient

# Initialize Flask app
app = Flask(__name__)

# Initialize GPT-4 client from gpt-4free
client = Client()

# Connect to MongoDB
mongo_client = MongoClient("mongodb://localhost:27017/")  # Ensure MongoDB is running locally
db = mongo_client["storydb"]  # Database name
stories_collection = db["stories"]  # Collection name

# Root route
@app.route("/")
def home():
    return "Welcome to the GPT-4 AI Storytelling Backend!"

# Route for generating a story
@app.route("/generate_story", methods=["POST"])
def generate_story():
    data = request.json
    prompt = data.get("prompt", "").strip()
    max_length = data.get("max_length", 200)  # Default maximum token length
    num_return_sequences = data.get("num_return_sequences", 1)  # Number of stories to generate
    temperature = data.get("temperature", 0.7)  # Creativity level
    mode = data.get("mode", "general")  # Default mode

    if not prompt:
        return jsonify({"error": "Prompt cannot be empty!"}), 400

    try:
        # Optionally modify the prompt based on the mode
        if mode == "fantasy":
            prompt = f"Fantasy: {prompt}"
        elif mode == "sci-fi":
            prompt = f"Sci-Fi: {prompt}"
        elif mode == "mystery":
            prompt = f"Mystery: {prompt}"
        # Add more modes as needed

        # Generate story using GPT-4
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
        )

        generated_story = response.choices[0].message.content

        return jsonify({"stories": [generated_story]})
    except Exception as e:
        return jsonify({"error": f"Story generation failed: {str(e)}"}), 500

# Route for saving a story to the database
@app.route("/save_story", methods=["POST"])
def save_story():
    data = request.json
    prompt = data.get("prompt", "").strip()
    story = data.get("story", "").strip()

    if not prompt or not story:
        return jsonify({"error": "Both prompt and story are required!"}), 400

    try:
        # Save story to MongoDB
        stories_collection.insert_one({"prompt": prompt, "story": story})
        return jsonify({"message": "Story saved successfully!"})
    except Exception as e:
        return jsonify({"error": f"Saving story failed: {str(e)}"}), 500

# Route for retrieving all saved stories
@app.route("/get_stories", methods=["GET"])
def get_stories():
    try:
        # Retrieve all stories from MongoDB
        stories = list(stories_collection.find({}, {"_id": 0}))  # Exclude MongoDB's internal _id field
        return jsonify({"stories": stories})
    except Exception as e:
        return jsonify({"error": f"Fetching stories failed: {str(e)}"}), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
