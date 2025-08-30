import random

quotes = [
    "You are strong. You are powerful. You are unstoppable.",
    "Your safety is your right. Speak up. Stay alert.",
    "You deserve to feel safe anywhere, anytime.",
    "Believe in yourself. You are never alone.",
    "Courage is not the absence of fear, but the triumph over it."
]

def get_motivational_quote():
    return random.choice(quotes)
