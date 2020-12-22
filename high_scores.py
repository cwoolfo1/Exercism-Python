def latest(scores):
    return scores[-1]

def personal_best(scores):
    scores = sorted(scores)
    return scores[len(scores)-1]

def personal_top_three(scores):
    return sorted(scores, reverse=True)[:3]
