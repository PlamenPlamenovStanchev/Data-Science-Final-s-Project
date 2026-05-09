"""Data-cleaning helpers for the sports injury project.

This module contains reusable preprocessing functions used by the data
preparation notebook. The helpers focus on text normalization, explicit missing
value handling, and NBA-specific injury keyword extraction from free-text notes.
"""

import pandas as pd
import re


def normalize_empty_strings(df, columns):
    """
    Converts empty strings in selected DataFrame columns into explicit missing values.

    Text-cleaning steps can remove punctuation, numbers, or extra spaces and leave
    behind empty strings. Pandas does not automatically treat those empty strings
    as missing data, so this helper standardizes them as `pd.NA` before later
    filtering, validation, or aggregation.

    Args:
        df (pd.DataFrame): Dataset that contains the columns to inspect.
        columns (list): Column names where empty strings should be treated as missing values.

    Returns:
        pd.DataFrame: The same dataset with empty strings replaced by `pd.NA`
        in the selected columns.
    """
    # Process only the columns requested by the cleaning step.
    for col in columns:
        # Skip missing column names so the helper can be reused across datasets.
        if col in df.columns:
            # Mark blank strings as true missing values for reliable dropna/isnull checks.
            df[col] = df[col].replace("", pd.NA)

    return df


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
    Extracts the most relevant injury keyword from an NBA free-text note.

    The NBA dataset stores injury information in narrative notes instead of a
    dedicated anatomical field. This helper keeps the extracted `injury_type`
    more informative by checking a broader set of common basketball injury terms
    before falling back to non-injury or unknown labels.
    
    Args:
        note (str or NaN): The raw injury note/description.
        
    Returns:
        str: A standardized injury keyword such as 'knee', 'ankle', 'illness',
        'rest', 'unknown', or 'other' if no keyword matched.
    """
    # Preprocess the note to ensure uniform matching
    note = clean_text(note)
    
    # Return 'unknown' if there is no note to process
    if pd.isna(note):
        return "unknown"
    
    # Categorize the injury based on specific keywords in the note.
    if any(word in note for word in ["concussion", "head", "face", "jaw", "nose", "eye"]):
        return "head"
    elif "knee" in note or "acl" in note or "mcl" in note:
        return "knee"
    elif "ankle" in note:
        return "ankle"
    elif "foot" in note or "heel" in note or "toe" in note:
        return "foot"
    elif "hamstring" in note:
        return "hamstring"
    elif "hip" in note:
        return "hip"
    elif "groin" in note or "adductor" in note:
        return "groin"
    elif "quad" in note or "quadriceps" in note or "thigh" in note:
        return "quad"
    elif "calf" in note or "achilles" in note or "shin" in note:
        return "lower leg"
    elif "shoulder" in note:
        return "shoulder"
    elif "back" in note or "spine" in note or "lumbar" in note:
        return "back"
    elif "neck" in note:
        return "neck"
    elif "wrist" in note:
        return "wrist"
    elif "hand" in note or "finger" in note or "thumb" in note:
        return "hand"
    elif "elbow" in note or "forearm" in note or "arm" in note:
        return "arm"
    elif "rib" in note or "chest" in note:
        return "chest"
    elif "abdominal" in note or "abdomen" in note or "oblique" in note or "core" in note:
        return "core"
    elif any(word in note for word in ["illness", "flu", "covid", "virus", "infection"]):
        return "illness"
    elif any(word in note for word in ["rest", "personal", "load management", "dnp"]):
        return "rest"
    elif any(word in note for word in ["unknown", "undisclosed", "not disclosed"]):
        return "unknown"
    else:
        return "other"
