leaderboard = []

def add_score(name, score):
    leaderboard.append((name, score))
    leaderboard.sort(key=lambda x: x[1], reverse=True)

def get_scores():
    return leaderboard[:10]
