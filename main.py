from model import load_model
from gui import start_gui

def main():
    print("Hi there")
    model = load_model()
    start_gui(model)

main()