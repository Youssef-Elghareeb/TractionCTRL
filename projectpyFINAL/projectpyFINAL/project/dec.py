def color_decorator(color: str):
    """Decorator that wraps a function and prints its output in ANSI color."""
    colors = {
        "red": "\033[91m",
        "orange": "\033[38;5;208m",
        "yellow": "\033[93m",
        "green": "\033[92m",
        "blue": "\033[94m",
        "pink": "\033[95m",
        "purple": "\033[38;5;54m",
        "reset": "\033[0m"
    }

    def decorator(func):
        def wrapper(*args, **kwargs):
            color_code = colors.get(color.lower(), colors["reset"])
            result = func(*args, **kwargs)
            return f"{color_code}{result}{colors['reset']}"
        return wrapper

    return decorator
