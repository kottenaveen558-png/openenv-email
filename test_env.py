from env import EmailEnv
from models import TriageAction

env = EmailEnv()

# Start environment
obs = env.reset()
print("Initial Observation:", obs)

done = False

while not done:
    # Dummy action (you can change values)
    action = TriageAction(
        category="spam",
        priority="low",
        action="ignore"
    )

    obs, reward, done, _ = env.step(action)

    print("\nNext Observation:", obs)
    print("Reward:", reward)

print("\nEnvironment finished successfully ✅")