def is_palindrome(s):
    """
    Sprawdza, czy podany ciąg znaków jest palindromem.
    Ignoruje spacje, wielkość liter i znaki interpunkcyjne.
    """
    import re

    # Usuwanie spacji i znaków interpunkcyjnych oraz konwersja na małe litery
    cleaned_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

    # Sprawdzenie, czy ciąg jest palindromem
    return cleaned_s == cleaned_s[::-1]



print(is_palindrome(''))