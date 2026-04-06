import os
from openai import OpenAI
from env import EmailEnv
from models import TriageAction

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def run():
    env = EmailEnv()
    obs = env.reset()

    total_score = 0
    done = False

    while not done:
        prompt = f"""
        You are an email triage assistant.

        Email:
        {obs}

        Decide:
        - category
        - priority
        - action (reply/ignore/escalate)

        Return JSON like:
        {{
            "category": "...",
            "priority": "...",
            "action": "..."
        }}
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        output = response.choices[0].message.content

        # ⚠️ For now assume model returns correct JSON (we improve later)
        action_dict = eval(output)

        action = TriageAction(**action_dict)

        obs, reward, done, _ = env.step(action)

        total_score += reward.score

    print("Final Score:", total_score)


if __name__ == "__main__":
    run()