import time
import random
from datetime import datetime

users = ['alice', 'bob', 'charlie', 'dave', 'eve', 'frank', 'grace', 'heidi', 'ivan', 'judy']
actions = ['login', 'logout', 'purchase', 'view', 'click', "file_upload", "file_download"]

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
        yield event
        time.sleep(delay)