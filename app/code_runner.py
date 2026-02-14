import subprocess
import tempfile
import os

def run_python(code: str):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".py", mode="w", encoding="utf-8") as f:
        f.write(code)
        temp = f.name

    try:
        result = subprocess.run(
            ["python", temp],
            capture_output=True,
            text=True,
            timeout=3,
            input=""
        )
        return result.stdout, result.stderr

    except subprocess.TimeoutExpired:
        return "", "Program requires user input or runs too long. Execution skipped for safety."


    except Exception as e:
        return "", f"Execution error: {str(e)}"

    finally:
        if os.path.exists(temp):
            os.remove(temp)
