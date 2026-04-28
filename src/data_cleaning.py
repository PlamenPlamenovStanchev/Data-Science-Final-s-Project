import pandas as pd
import re

def clean_text(text):
    if pd.isna(text):
        return text
    
    text = str(text).lower().strip()
    text = re.sub(r"[^a-z\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    
    return text


def extract_nba_injury_type(note):
    note = clean_text(note)
    
    if pd.isna(note):
        return "unknown"
    
    if "concussion" in note or "head" in note:
        return "head"
    elif "ankle" in note:
        return "ankle"
    elif "knee" in note:
        return "knee"
    elif "shoulder" in note:
        return "shoulder"
    elif "back" in note:
        return "back"
    elif "hamstring" in note:
        return "hamstring"
    elif "foot" in note:
        return "foot"
    elif "hip" in note:
        return "hip"
    elif "wrist" in note:
        return "wrist"
    elif "illness" in note or "flu" in note:
        return "illness"
    elif "rest" in note:
        return "rest"
    else:
        return "other"