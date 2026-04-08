import gradio as gr
from env import EmailEnv
from models import TriageAction

def process_email(text):
    env = EmailEnv()
    env.reset()

    # Simple logic (you can improve later)
    if "offer" in text.lower():
        action = TriageAction(category="spam", priority="low", action="ignore")
    else:
        action = TriageAction(category="important", priority="high", action="read")

    obs, reward, done, info = env.step(action)

    return f"""
Category: {action.category}
Priority: {action.priority}
Action: {action.action}
Reward: {reward.score}
"""

iface = gr.Interface(
    fn=process_email,
    inputs="text",
    outputs="text",
    title="OpenEnv Email AI",
    description="AI agent that classifies and takes action on emails"
)

iface.launch()