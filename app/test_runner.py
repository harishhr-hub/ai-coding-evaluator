import subprocess
import tempfile
import os

def run_tests(code: str, test_cases):
    passed = 0

    with tempfile.NamedTemporaryFile(delete=False, suffix=".py", mode="w", encoding="utf-8") as f:
        f.write(code)
        temp = f.name

    try:
        for inp, expected in test_cases:
            try:
                result = subprocess.run(
                    ["python", temp],
                    input=inp,
                    capture_output=True,
                    text=True,
                    timeout=2
                )
                if result.stdout.strip() == expected:
                    passed += 1
            except:
                continue
    finally:
        os.remove(temp)

    return passed, len(test_cases)


