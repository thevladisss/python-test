# gui.py
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from model import classify_image

def start_gui(model):
    # Initialize the main window
    root = tk.Tk()
    root.title("Image Recognition App")

    # Function to upload and classify image
    def upload_and_classify():
        file_path = filedialog.askopenfilename()
        if file_path:
            img = Image.open(file_path)
            img = img.resize((224, 224))  # Resize for display in the GUI
            img_tk = ImageTk.PhotoImage(img)
            panel.config(image=img_tk)
            panel.image = img_tk

            # Use the model to classify the image
            predictions = classify_image(model, file_path)
            result_text.set("\n".join([f"{p[1]}: {p[2]*100:.2f}%" for p in predictions]))

    # GUI layout
    result_text = tk.StringVar()
    panel = tk.Label(root)
    panel.pack(side="top", fill="both", expand="yes")

    # Upload button
    tk.Button(root, text="Upload Image", command=upload_and_classify).pack(side="bottom")
    tk.Label(root, textvariable=result_text).pack(side="bottom")

    # Start the Tkinter loop
    root.mainloop()
