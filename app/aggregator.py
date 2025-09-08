#In-memory storage
events = []

def add_events(event):
    """Add an event to the in-memory storage"""
    events.append(event)
    
def get_user_event_counts():
    """Return count of events per user as a dictionary"""
    counts = {}
    for e in events:
        counts[e["user"]] = counts.get(e["user"], 0) + 1
    return counts

def get_action_counts():
    """Return count of each action type"""
    counts = {}
    
    for e in events:
        counts[e["action"]] = counts.get(e["action"], 0) + 1
    return counts

def get_latest_timestamp_per_user():
    """Return the most recent timestamp for each user"""
    latest = {}
    for e in events:
        user = e["user"]
        ts = e["timestamp"]
        if user not in latest or ts > latest[user]:
            latest[user] = ts
    return latest