import time
import random
import requests
from datetime import datetime

users = ['alice', 'bob', 'charlie', 'dave', 'eve', 'frank', 'grace', 'heidi', 'ivan', 'judy']
actions = ['login', 'logout', 'purchase', 'view', 'click', "file_upload", "file_download"]

API_URL = "http://127.0.0.1:8000/events"

def generate_event(event_id):
    """Generate a random event
    Args: event_id (int): Unique identifier for the event
    Returns: dict: A dictionary representing the event
    """
    return {
        "user_id": random.choice(users),   
        "action": random.choice(actions),
        "timestamp": datetime.utcnow().isoformat()
    }
    
def event_stream(n=10, delay=0.5):
    """Simulate n events with optional delay in seconds
    Args: n: int: Number of events to generate
          delay: float: Delay in seconds between events
    Yields: dict: Event Dictionaries"""
    for i in range(1, n+1):
        event = generate_event(i)
        print(f"Generated event: {event}")
        response = requests.post(API_URL, json=event)
        print("Server response:", response.json())
        time.sleep(delay)
        
if __name__ == "__main__":
    event_stream(n=20, delay=1)  # Generate 20 events with a 1 second delay between them