import os
from tkinter import filedialog
from PIL import Image
from docx import Document

def upload_image():
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")]
    )
    return file_path

def save_image(image, save_path):
    image.save(save_path)

def save_text_to_docx(text):
    file_path = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word Document", "*.docx")])
    if file_path:
        try:
            doc = Document()
            doc.add_paragraph(text)
            doc.save(file_path)
            return True, ""
        except Exception as e:
            return False, str(e)
    return False, "No file path selected."
