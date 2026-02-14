import re

def readability_score(code: str):
    score = 100

    # Penalize short variable names
    short_vars = re.findall(r"\b[a-zA-Z]{1}\b", code)
    score -= len(short_vars) * 2

    # Penalize lack of comments
    if "#" not in code:
        score -= 15

    return max(score, 40)


def complexity_estimate(code: str):
    loops = code.count("for ") + code.count("while ")
    if loops >= 2:
        return "O(n²)", 70
    elif loops == 1:
        return "O(n)", 85
    else:
        return "O(1)", 95
