# Create A virtual Environment for this application
python -m venv venv

# To activate in Terminal (re-activate before running the server)
.\venv\Scripts\Activate

# Install dependencies inside venv
pip install fastapi uvicorn requests

# Run the server
python -m uvicorn app.main:app --reload

navigate to http://127.0.0.1:8000/docs to view FastAPI