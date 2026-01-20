# mylib.py — a tiny demo library for beginners


LIB_NAME = "TinyTools"

def greeti(name):
    return "Hello, " + name + "! 👋"

def add(a, b):
    return a + b

def mood(n):
    # simple, playful mapping 1..3
    if n == 1:
        return "Calm 🌊"
    elif n == 2:
        return "Curious 🧭"
    else:
        return "Cheerful ☀️"

# Quick self-test if you run this file directly:
if __name__ == "__main__":
    print("Running", APP_NAME)
    print(greeti("Coder"))
    print("2 + 3 =", add(2, 3))
    print("Mood(2):", mood(2))