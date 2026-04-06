def grade_classification(action, email):
    return 1.0 if action.category == email["category"] else 0.0


def grade_priority(action, email):
    return 1.0 if action.priority == email["priority"] else 0.0


def grade_full(action, email):
    score = 0.0

    if action.category == email["category"]:
        score += 0.3

    if action.priority == email["priority"]:
        score += 0.3

    if action.action == email["correct_action"]:
        score += 0.4

    return score