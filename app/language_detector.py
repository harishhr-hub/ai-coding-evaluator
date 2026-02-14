def detect_language(filename: str, code: str):
    if filename.endswith(".py"):
        return "Python"
    if filename.endswith(".cpp"):
        return "C++"
    if filename.endswith(".java"):
        return "Java"
    if "#include" in code:
        return "C++"
    if "import java" in code:
        return "Java"
    return "Python"
