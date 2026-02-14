import difflib

def similarity(code1, code2):
    return round(difflib.SequenceMatcher(None, code1, code2).ratio() * 100, 2)
