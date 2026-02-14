# Code Evaluator API

A FastAPI-based application that analyzes code for readability, modularity, efficiency, and edge-case handling. It supports both GitHub repository links and direct file uploads, providing detailed feedback and a downloadable PDF report.

## Features

- **Code Analysis**: Evaluates code based on multiple metrics:
  - **Readability**: Checks for comments and variable naming.
  - **Modularity**: Analyzes function definitions.
  - **Efficiency**: Detects time complexity (O(1), O(n), O(n²)).
  - **Edge Case Handling**: Looks for input validation and checks.
- **GitHub Integration**: Fetches raw code directly from GitHub URLs.
- **File Upload**: Supports direct upload of source files for analysis.
- **PDF Report Generation**: Generates a professional PDF summary of the evaluation.
- **Web Interface**: Simple and intuitive UI built with Jinja2 templates.

## Tech Stack

- **Backend**: FastAPI (Python)
- **Templating**: Jinja2
- **PDF Generation**: ReportLab
- **HTTP Client**: Requests
- **Server**: Uvicorn

## Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd AI_Coding/app
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

Start the server using Uvicorn:

```bash
uvicorn main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

## Usage

1. Open the home page.
2. Provide a **GitHub File URL** or **Upload a Python File**.
3. Click **Evaluate** to see the scores and feedback.
4. Click **Download PDF Report** to save the results locally.

## Project Structure

- `main.py`: Core logic and API endpoints.
- `report_generator.py`: PDF generation logic using ReportLab.
- `templates/`: HTML templates for the web interface.
- `requirements.txt`: Project dependencies.
