def categorize_injury(injury):
    """
    Map granular injury descriptions to broad anatomical categories.
    
    Consolidates diverse injury terminology from multiple sports datasets into four 
    standardized anatomical categories:
    - "Head": Head/neurological injuries
    - "Upper Body": Shoulder, arm, chest, back, and related injuries
    - "Lower Body": Knee, ankle, hip, leg, and related injuries
    - "Other": Non-injury statuses (rest, illness) and unclassified injuries
    
    Uses case-insensitive keyword matching on the injury string.
    
    Args:
        injury: Raw injury description (str, int, float, or None). Handles None safely.
    
    Returns:
        str: One of four categories: "Head", "Upper Body", "Lower Body", or "Other".
    """
    if injury is None:
        return "Other"
    
    injury = str(injury).lower()

    # HEAD
    if any(word in injury for word in [
        "concussion", "head", "brain", "face", "jaw", "nose"
    ]):
        return "Head"

    # LOWER BODY INJURIES
    elif any(word in injury for word in [
        "knee", "ankle", "foot", "toe", "leg", "hamstring",
        "groin", "hip", "thigh", "calf", "achilles",
        "lower body"
    ]):
        return "Lower Body"

    # UPPER BODY INJURIES
    elif any(word in injury for word in [
        "shoulder", "arm", "elbow", "wrist", "hand",
        "finger", "chest", "rib", "back", "spine",
        "upper body"
    ]):
        return "Upper Body"

    # NON-INJURY IMPORTANT FOR NBA
    elif any(word in injury for word in [
        "rest", "illness", "flu", "covid", "personal", "dnp"
    ]):
        return "Other"

    else:
        return "Other"