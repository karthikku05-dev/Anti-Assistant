<img width="1280" height="640" alt="git (1)" src="https://github.com/user-attachments/assets/8920b256-2ba8-4988-b824-5351134eb4bd" />



# The Anti-Assistant 🎯


## Basic Details
### Team Name: [Add team name]


### Team Members
- Team Lead: [Add name] - [Add college]
- Member 2: [Add name] - [Add college]
- Member 3: [Add name] - [Add college]

### Project Description
The Anti-Assistant is a deliberately unhelpful AI chat application. It responds to ordinary questions with short, technically accurate, deadpan answers that follow the literal wording instead of providing the practical help the user expected.

The project combines a lightweight FastAPI service with a browser-based chat interface and Google's Gemini API.

### The Problem (that doesn't exist)
People keep asking assistants useful questions and receiving useful answers. This project addresses the much less urgent problem of assistants being helpful when they could instead be pedantic, irrelevant, and completely accurate.

### The Solution (that nobody asked for)
The backend sends each inquiry to Gemini with an Anti-Assistant system prompt. The prompt enforces literal interpretations, absurd comparisons, irrelevant trivia, and short deadpan responses, while the frontend presents the exchange as a simple support-ticket-style chat.

## Technical Details
### Technologies/Components Used
For Software:
- Python
- HTML, CSS, and JavaScript
- FastAPI and Uvicorn
- Pydantic
- Google Gen AI SDK (`google-genai`)
- `python-dotenv` for local environment configuration
- Git and GitHub

For Hardware:
- No hardware required
- Runs in a web browser with a Python backend

### Implementation
For Software:
# Installation
Clone the repository and move into the project directory:

```bash
git clone https://github.com/karthikku05-dev/Anti-Assistant.git
cd Anti-Assistant
```

Install the Python dependencies:

```bash
pip install fastapi uvicorn python-dotenv google-genai pydantic
```

Create a `.env` file in the project root. Do not commit this file:

```dotenv
GEMINI_API_KEY=your_gemini_api_key_here
```

The repository includes `.env.example` as a safe configuration template.

# Run
Start the development server:

```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

Open [http://localhost:8000](http://localhost:8000) in a browser.

### Project Documentation
For Software:

# Screenshots (Add at least 3)
![Screenshot1](Add screenshot of the Anti-Assistant chat interface here)
*The browser-based chat interface for submitting inquiries and viewing responses.*

![Screenshot2](Add screenshot of a generated response here)
*An example of the assistant's technically accurate but unhelpful response style.*

![Screenshot3](Add screenshot of the responsive layout here)
*The chat layout running in a browser viewport.*

# Diagrams
![Workflow](Add workflow diagram here)
*User inquiry -> browser `fetch` request -> FastAPI `/api/chat` endpoint -> Gemini API -> response displayed in the chat.*

For Hardware:

# Schematic & Circuit
![Circuit](Add your circuit diagram here)
*Add caption explaining connections*

![Schematic](Add your schematic diagram here)
*Add caption explaining the schematic*

# Build Photos
![Components](Add photo of your components here)
*List out all components shown*

![Build](Add photos of build process here)
*Explain the build steps*

![Final](Add photo of final product here)
*Explain the final build*

### Project Demo
# Video
[Add demo video link here]
*The demo should show the server starting, the chat interface loading, and an inquiry receiving an Anti-Assistant response.*

# Additional Demos
[Add any extra demo materials or links here]

## Team Contributions
- [Add name]: FastAPI backend, Gemini integration, and prompt design
- [Add name]: Frontend chat interface and interaction logic
- [Add name]: Testing, documentation, and project presentation

---
Made with ❤️ at TinkerHub Useless Projects 

![Static Badge](https://img.shields.io/badge/TinkerHub-24?color=%23000000&link=https%3A%2F%2Fwww.tinkerhub.org%2F)
![Static Badge](https://img.shields.io/badge/UselessProjects--26-26?link=https%3A%2F%2Ftinkerhub.org%2Fevents%2F1M8ORET9A1%2Fuseless-projects-3.0)



