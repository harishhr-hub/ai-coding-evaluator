import requests

def fetch_code_from_github(url: str):
    if "github.com" in url:
        url = url.replace("github.com", "raw.githubusercontent.com")
        url = url.replace("/blob/", "/")

    r = requests.get(url)
    if r.status_code != 200:
        raise Exception("Failed to fetch file")
    return r.text
