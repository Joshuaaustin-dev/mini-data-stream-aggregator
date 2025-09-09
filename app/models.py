from pydantic import BaseModel

class Event(BaseModel):
    user_id: str
    action: str
    timestamp: str
