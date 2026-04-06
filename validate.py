from env import EmailEnv
from models import TriageAction

def validate():
    env = EmailEnv()

    # Test reset
    obs = env.reset()
    assert obs is not None, "Reset failed"

    # Test state
    state = env.state()
    assert state is not None, "State failed"

    done = False
    steps = 0

    while not done:
        action = TriageAction(
            category="spam",
            priority="low",
            action="ignore"
        )

        obs, reward, done, info = env.step(action)

        # Validate outputs
        assert reward is not None, "Reward missing"
        assert hasattr(reward, "score"), "Reward score missing"

        steps += 1

        if steps > 50:
            break

    print("✅ Validation Passed")

if __name__ == "__main__":
    validate()