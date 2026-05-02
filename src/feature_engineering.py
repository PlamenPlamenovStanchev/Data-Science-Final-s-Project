def categorize_injury(injury):
    """
    Categorizes a specific injury description into broad anatomical groups.
    
    This function analyzes an injury string and maps it to a generalized category 
    such as 'Head', 'Lower Body', or 'Upper Body' based on recognized keywords. 
    It also handles non-injury occurrences (e.g., rest, illness) by grouping them
    under 'Other'. If the injury is unrecognized, missing, or none of the 
    keywords match, it defaults to returning 'Other'.
    
    Args:
        injury (str or None): The specific injury description or type.
        
    Returns:
        str: A broader anatomical category for the injury ('Head', 'Lower Body', 
             'Upper Body', or 'Other').
    """
    if injury is None:
        return "Other"
    
    injury = str(injury).lower()

    # HEAD INJURIES
    if any(word in injury for word in [
        "concussion", "head", "brain", "face", "jaw", "nose"
    ]):
        return "Head"

    # LOWER BODY INJURIES
    elif any(word in injury for word in [
        "knee", "ankle", "foot", "toe", "leg", "hamstring",
        "groin", "hip", "thigh", "calf", "achilles"
    ]):
        return "Lower Body"

    # UPPER BODY INJURIES
    elif any(word in injury for word in [
        "shoulder", "arm", "elbow", "wrist", "hand",
        "finger", "chest", "rib", "back", "spine"
    ]):
        return "Upper Body"

    # NON-INJURY (e.g., rest, illness, important for NBA dataset)
    elif any(word in injury for word in [
        "rest", "illness", "flu", "covid", "personal"
    ]):
        return "Other"

    else:
        return "Other"