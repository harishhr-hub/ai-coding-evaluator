from fastapi import FastAPI, Form, Request, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse
from report_generator import create_report

import requests
import re

app = FastAPI()
templates = Jinja2Templates(directory="templates")


# -----------------------------
# Utility functions (inline so nothing breaks)
# -----------------------------

def fetch_code_from_github(url: str):
    if "github.com" in url:
        url = url.replace("github.com", "raw.githubusercontent.com")
        url = url.replace("/blob/", "/")
    r = requests.get(url)
    if r.status_code != 200:
        raise Exception("Could not fetch GitHub file")
    return r.text


def readability(code):
    score = 100
    if "#" not in code:
        score -= 10
    short_vars = re.findall(r"\b[a-zA-Z]{1}\b", code)
    score -= len(short_vars) * 2
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


def final_score(corr, eff, read, mod, edge):
    total = (
        corr * 0.35 +
        eff * 0.20 +
        read * 0.15 +
        mod * 0.15 +
        edge * 0.15
    )
    return int(total)


def generate_feedback(scores, complexity, code):
    return f"""
Overall Score: {scores['total']}/100

Correctness: {scores['correctness']}
Efficiency: {scores['efficiency']}
Readability: {scores['readability']}
Modularity: {scores['modularity']}
Edge Handling: {scores['edge']}

Detected Complexity: {complexity}

Suggestions:
• Improve variable naming clarity
• Add comments explaining logic
• Optimize nested loops if present
• Handle empty inputs and edge cases
• Break logic into reusable functions
"""


# -----------------------------
# Routes
# -----------------------------

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/evaluate", response_class=HTMLResponse)
async def evaluate(request: Request,
                   github_url: str = Form(None),
                   file: UploadFile = File(None)):

    try:
        # Load code
        if github_url:
            code = fetch_code_from_github(github_url)
        elif file:
            code = (await file.read()).decode()
        else:
            return templates.TemplateResponse(
                "index.html",
                {"request": request,
                 "result": "Please upload a file or paste GitHub file URL."}
            )

        # Evaluate
        read = readability(code)
        mod = modularity(code)
        comp, eff = complexity(code)
        edge = edge_case_score(code)
        correctness = 80

        total_score = final_score(correctness, eff, read, mod, edge)

        scores = {
            "correctness": correctness,
            "efficiency": eff,
            "readability": read,
            "modularity": mod,
            "edge": edge,
            "total": total_score
        }

        feedback = generate_feedback(scores, comp, code)
        # Create PDF file every time evaluation runs
        create_report("report.pdf", feedback)


        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "result": feedback,
                "scores": scores,
                "code": code
            }
        )

    except Exception as e:
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "result": f"System error: {str(e)}"
            }
        )
@app.get("/report")
def get_report():
    return FileResponse(
        path="report.pdf",
        filename="evaluation_report.pdf",
        media_type='application/pdf'
    )
