# Mini Data Stream Aggregator
A lightweight FastAPI application that takes in user events in real time and tracks metrics such as:

- Event counts per user
- Counts per action type
- Latest event timestamp per user

---

## Features
- REST API with FastAPI
- In-memory storage for quick prototyping
- Event simulator for generating test data
- Metrics endpoint for analytics
- Unit Testing with Pytest

---

### Installation
1. Clone the repository

2. Create A virtual Environment for this application
python -m venv venv
source venv/Scripts/activate       # Windows
source venv/bin/activate           # Mac/Linux

3. To activate in Terminal (re-activate before running the server)
.\venv\Scripts\Activate

4. Install dependencies inside venv
pip install -r requirements.txt

# Run the server
python -m uvicorn app.main:app --reload

navigate to http://127.0.0.1:8000/docs to view FastAPI