def categorize_injury(injury):
    """
    Categorizes a specific injury description into broad anatomical groups.
    
    This function takes an injury string and maps it to a generalized category 
    such as 'Head', 'Lower Body', or 'Upper Body' based on recognized keywords. 
    If the injury is unrecognized, missing, or none of the keywords match, 
    it defaults to returning 'Other'.
    
    Args:
        injury (str or None): The specific injury description or type.
        
    Returns:
        str: A generalized category for the injury ('Head', 'Lower Body', 'Upper Body', or 'Other').
    """
    if injury is None:
        return "Other"
    
    injury = str(injury).lower()
    
    # HEAD INJURIES
    if any(word in injury for word in ["head", "concussion", "brain", "face"]):
        return "Head"
    
    # LOWER BODY INJURIES
    elif any(word in injury for word in ["knee", "ankle", "leg", "foot", "hamstring", "groin", "hip"]):
        return "Lower Body"
    
    # UPPER BODY INJURIES
    elif any(word in injury for word in ["shoulder", "arm", "elbow", "wrist", "hand", "chest", "back"]):
        return "Upper Body"
    
    else:
        return "Other"