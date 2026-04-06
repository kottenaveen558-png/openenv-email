from pydantic import BaseModel

class EmailObservation(BaseModel):
    email_text: str
    sender: str


class TriageAction(BaseModel):
    category: str
    priority: str
    action: str   # reply / ignore / escalate


class RewardBreakdown(BaseModel):
    score: float
    reason: str