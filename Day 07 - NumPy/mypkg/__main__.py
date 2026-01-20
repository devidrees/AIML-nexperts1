# Lets you run the package directly:  python -m mypkg
from .tools import APP_NAME, greet

if __name__ == "__main__":
    print("Running", APP_NAME)
    print(greet("World"))

def hinum(num):
    return num
