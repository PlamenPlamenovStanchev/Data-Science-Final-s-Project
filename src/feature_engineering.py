import re


REST_KEYWORDS = [
    "rest", "rested", "resting", "load management", "personal",
    "dnp", "inactive", "not with team"
]

ILLNESS_KEYWORDS = [
    "illness", "flu", "virus", "viral", "covid", "covid related",
    "infection", "sick", "migraine"
]

UNKNOWN_KEYWORDS = [
    "unknown", "undisclosed", "misc", "misc unk", "not disclosed",
    "unspecified", "general soreness"
]

HEAD_KEYWORDS = [
    "concussion", "head", "brain", "face", "facial", "jaw", "nose",
    "eye", "orbital", "mouth", "dental", "tooth", "teeth", "ear"
]

LOWER_BODY_KEYWORDS = [
    "knee", "ankle", "foot", "feet", "toe", "leg", "hamstring",
    "groin", "hip", "thigh", "calf", "achilles", "quad",
    "quadriceps", "shin", "heel", "adductor", "glute", "glutes",
    "pelvis", "lower body", "lower leg", "plantar", "meniscus",
    "acl", "mcl", "patella", "tibia", "fibula"
]

UPPER_BODY_KEYWORDS = [
    "shoulder", "arm", "elbow", "wrist", "hand", "finger", "thumb",
    "chest", "rib", "ribs", "back", "spine", "neck", "abdomen",
    "abdominal", "oblique", "core", "forearm", "biceps", "triceps",
    "pectoral", "pec", "lat", "upper body", "upper arm", "lumbar",
    "thoracic"
]


def _compile_keyword_pattern(keywords):
    escaped_keywords = [re.escape(keyword) for keyword in keywords]
    return re.compile(r"\b(?:" + "|".join(escaped_keywords) + r")\b")


REST_PATTERN = _compile_keyword_pattern(REST_KEYWORDS)
ILLNESS_PATTERN = _compile_keyword_pattern(ILLNESS_KEYWORDS)
UNKNOWN_PATTERN = _compile_keyword_pattern(UNKNOWN_KEYWORDS)
HEAD_PATTERN = _compile_keyword_pattern(HEAD_KEYWORDS)
LOWER_BODY_PATTERN = _compile_keyword_pattern(LOWER_BODY_KEYWORDS)
UPPER_BODY_PATTERN = _compile_keyword_pattern(UPPER_BODY_KEYWORDS)


def categorize_injury(injury):
    """
    Map injury descriptions into broader analysis categories.

    The function uses keyword matching over the available injury text and returns
    anatomical categories when a body area is detected. It also separates common
    non-anatomical statuses such as illness, rest, and unknown/undisclosed cases
    so they do not inflate the generic "Other" category.

    Args:
        injury (str or NaN): Cleaned injury text, raw notes, or combined injury context.

    Returns:
        str: One of "Head", "Upper Body", "Lower Body", "Illness",
        "Rest/Non-injury", "Unknown", or "Other".
    """
    if injury is None or injury != injury:
        return "Unknown"

    injury = str(injury).lower().strip()

    if not injury:
        return "Unknown"

    # Non-injury and ambiguous statuses should not be mixed with true injury misses.
    if REST_PATTERN.search(injury):
        return "Rest/Non-injury"

    if ILLNESS_PATTERN.search(injury):
        return "Illness"

    if UNKNOWN_PATTERN.search(injury):
        return "Unknown"

    if HEAD_PATTERN.search(injury):
        return "Head"

    if LOWER_BODY_PATTERN.search(injury):
        return "Lower Body"

    if UPPER_BODY_PATTERN.search(injury):
        return "Upper Body"

    return "Other"
