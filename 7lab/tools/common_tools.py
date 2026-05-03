"""Спільні інструменти для всіх агентів"""

def format_text(text: str, style: str = "uppercase") -> str:
    """Форматує текст за вказаним стилем."""
    if style == "uppercase":
        return text.upper()
    elif style == "lowercase":
        return text.lower()
    elif style == "title":
        return text.title()
    return text

def count_words(text: str) -> dict:
    """Підраховує кількість слів у тексті."""
    words = text.split()
    return {
        "total_words": len(words),
        "total_chars": len(text),
        "unique_words": len(set(words))
    }