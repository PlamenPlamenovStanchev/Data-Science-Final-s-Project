import pandas as pd
import re

def clean_text(text):
    """
    Cleans the input text by converting to lowercase, removing non-alphabetic 
    characters, and normalizing whitespace.
    
    Args:
        text (str or NaN): The raw text string to be cleaned.
        
    Returns:
        str or NaN: The cleaned string, or NaN if the input was missing.
    """
    # Return immediately if the text is null/NaN
    if pd.isna(text):
        return text
    
    # Convert to string, lowercase it, and remove leading/trailing whitespace
    text = str(text).lower().strip()
    
    # Replace all non-alphabetic characters (anything not a-z or whitespace) with a space
    text = re.sub(r"[^a-z\s]", " ", text)
    
    # Replace multiple contiguous spaces with a single space and trim edges again
    text = re.sub(r"\s+", " ", text).strip()
    
    return text


def extract_nba_injury_type(note):
    """
    Parses a raw injury note and categorizes it into a standard injury type 
    (e.g., 'knee', 'ankle', 'head').
    
    Args:
        note (str or NaN): The raw injury note/description.
        
    Returns:
        str: A standardized injury category, or 'unknown' if missing, 
             or 'other' if no keyword matched.
    """
    # Preprocess the note to ensure uniform matching
    note = clean_text(note)
    
    # Return 'unknown' if there is no note to process
    if pd.isna(note):
        return "unknown"
    
    # Categorize the injury based on specific keywords in the note
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