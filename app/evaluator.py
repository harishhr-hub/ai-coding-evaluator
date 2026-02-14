import re

def readability(code):
    score = 100

    if "#" not in code:
        score -= 10

    short_vars = re.findall(r"\b[a-zA-Z]{1}\b", code)
    score -= len(short_vars) * 2

    if "def " in code and "docstring" not in code:
        score -= 10

    return max(score, 50)


def modularity(code):
    funcs = code.count("def ")
    return min(100, 60 + funcs * 10)


def complexity(code):
    loops = code.count("for ") + code.count("while ")
    if loops >= 2:
        return "O(n²)", 70
    elif loops == 1:
        return "O(n)", 85
    else:
        return "O(1)", 95


def edge_case_score(code):
    score = 100
    if "if" not in code:
        score -= 20
    if "len(" not in code:
        score -= 10
    return score
