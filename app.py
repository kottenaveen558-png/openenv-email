import gradio as gr
from env import EmailEnv
from models import TriageAction

def process_email(text):
    env = EmailEnv()
    env.reset()

    if "offer" in text.lower() or "win" in text.lower():
        action = TriageAction(category="spam", priority="low", action="ignore")
    elif "urgent" in text.lower():
        action = TriageAction(category="incident", priority="high", action="escalate")
    else:
        action = TriageAction(category="general", priority="medium", action="reply")

    obs, reward, done, _ = env.step(action)

    return f"""
Category: {action.category}
Priority: {action.priority}
Action: {action.action}
Score: {reward.score}
"""

iface = gr.Interface(
    fn=process_email,
    inputs="text",
    outputs="text",
    title="Email AI",
    description="Simple Email Triage Agent"
)

iface.launch()