# Vespera-AI
### Vespera AI - README
### Vespera AI


Welcome to **Vespera AI**, an AI-powered storytelling web app! With Vespera, users can generate creative stories based on their prompts, choose storytelling modes, and save or view generated content for later use. This README provides details on the app, how to access it, and how to set up and run the backend and frontend.

---

## Features

- **Story Generation**: Create stories using AI by providing a custom prompt and selecting parameters like storytelling mode, length, and creativity.
- **Story Modes**: Choose from genres like Fantasy, Sci-Fi, Mystery, or General to customize your experience.
- **Save and View Stories**: Save your favorite stories and view them anytime with MongoDB integration.

---

## App Architecture

1. **Frontend**: Developed with **Streamlit**, providing an interactive user interface for prompt submission, viewing stories, and saving content.
2. **Backend**: Built with **Flask**, handling story generation using `gpt-4free` and managing story storage via MongoDB.

---

## Prerequisites

Ensure the following are installed on your system:

- **Python 3.8 or later**
- **MongoDB** (Running locally on `localhost:27017`)
- **Pip** (Python package manager)

---

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/username/vespera-ai.git
   cd vespera-ai
   ```

2. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure MongoDB is running locally:
   ```bash
   mongod --config /path/to/mongod.conf
   ```

---

## Running the Application

### 1. Start the Backend (Flask)

- Navigate to the project directory and run:
  ```bash
  python main.py
  ```
- The backend server will start at `http://127.0.0.1:5000`.

### 2. Start the Frontend (Streamlit)

- Open a new terminal window, navigate to the same directory, and run:
  ```bash
  streamlit run app.py
  ```
- The frontend will be accessible at `http://localhost:8501`.

---

## Usage

1. **Access the App**:
   - Open your web browser and go to `http://localhost:8501`.

2. **Generate Stories**:
   - Enter a prompt in the "Generate a Story" section.
   - Select a storytelling mode, adjust creativity and length parameters, and click **Generate Story**.

3. **Save Stories**:
   - After generating a story, click **Save Story** to store it in the database.

4. **View Saved Stories**:
   - Click **View Saved Stories** to retrieve all previously saved stories from MongoDB.

---

## Troubleshooting

1. **MongoDB Connection Issues**:
   - Ensure MongoDB is running and accessible at `localhost:27017`.
   - Check if the `storydb` database and `stories` collection are set up correctly.

2. **Backend Errors**:
   - Verify that the Flask backend is running without errors and reachable at `http://127.0.0.1:5000`.

3. **Frontend Issues**:
   - Ensure all dependencies for Streamlit are installed, and check for port conflicts on `8501`.

---

<<<<<<< HEAD
## License

This project is licensed under the MIT License.

---

Feel free to reach out with any questions or issues. Happy storytelling! 🌟
=======
Feel free to reach out with any questions or issues. Happy storytelling! 🌟
>>>>>>> dff0cdb6cc7f93929f0eb10030609824502f5df0
