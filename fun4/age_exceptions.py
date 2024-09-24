def categorize_by_age_except(age):
    if not isinstance(age,int):
        raise TypeError(f"integer number expected, got: {type(age).__name__} ")
    if 0 <= age <= 9:
        return "Child"
    elif 9 < age <= 18:
        return "Adolescent"
    elif 18 < age <= 65:
        return "Adult"
    elif 65 < age <= 150:
        return "Golden age"
    else:
        return f"Invalid age: {age}"

