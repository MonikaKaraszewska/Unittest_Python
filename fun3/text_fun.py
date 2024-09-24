def analyze_text(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    result = {
        "length": len(text),
        "words": len(text.split()),
        "uppercase": sum(1 for c in text if c.isupper()),
        "lowercase": sum(1 for c in text if c.islower()),
        "digits": sum(1 for c in text if c.isdigit()),
        "spaces": text.count(' '),
        "most_common": max(set(text.lower()), key=text.lower().count) if text else None
    }

    return result

