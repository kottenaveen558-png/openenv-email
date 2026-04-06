from models import EmailObservation, TriageAction, RewardBreakdown
EMAILS = [
    {
        "email_text": "URGENT: Production server is down. Customers cannot login.",
        "sender": "ops@company.com",
        "priority": "high",
        "category": "incident",
        "correct_action": "escalate"
    },
    {
        "email_text": "You have won $10,000! Click here now!",
        "sender": "lottery@spam.com",
        "priority": "low",
        "category": "spam",
        "correct_action": "ignore"
    },
    {
        "email_text": "Requesting refund for incorrect billing this month.",
        "sender": "customer@gmail.com",
        "priority": "medium",
        "category": "billing",
        "correct_action": "reply"
    },
    {
        "email_text": "Please delete all my data under GDPR.",
        "sender": "user@domain.com",
        "priority": "high",
        "category": "legal",
        "correct_action": "escalate"
    },
    {
        "email_text": "Interested in your product demo. Please schedule a call.",
        "sender": "client@company.com",
        "priority": "medium",
        "category": "sales",
        "correct_action": "reply"
    }
]
class EmailEnv:
    def __init__(self):
        self.index = 0

    def reset(self):
        self.index = 0
        return self._get_observation()

    def step(self, action: TriageAction):
        current_email = EMAILS[self.index]
        reward = self._calculate_reward(action, current_email)

        self.index += 1
        done = self.index >= len(EMAILS)

        next_obs = self._get_observation() if not done else None

        return next_obs, reward, done, {}

    def state(self):
        return self._get_observation()
    
    def _get_observation(self):
        email = EMAILS[self.index]
        return EmailObservation(
            email_text=email["email_text"],
            sender=email["sender"]
        )
    def _calculate_reward(self, action: TriageAction, email):
        score = 0.0
        reason = []

        if action.action == email["correct_action"]:
            score += 0.5
            reason.append("correct action")

        if action.priority == email["priority"]:
            score += 0.3
            reason.append("correct priority")

        if action.category == email["category"]:
            score += 0.2
            reason.append("correct category")

        return RewardBreakdown(score=score, reason=", ".join(reason))
            

    