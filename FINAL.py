import cv2#open cv
import pytesseract
from PIL import Image
from matplotlib import pyplot as plt
import tkinter as tk
from tkinter import ttk,Toplevel,filedialog,messagebox
import time
from docx import Document

#------------------------------------------------------------------------------------------------------------------------------------------------------------

def upload_image():
    # Open file dialog to select an image
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")]
    )
    
    if file_path:
        try:
            # Open and load the image
            img = Image.open(file_path)
            img.save("process.jpg")  # Save it as process.jpg in the current directory
            messagebox.showinfo("Success", "Image Sent for processing")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to process the image: {e}")
    
    # After saving the image, we close the Tkinter window
    root.quit()

#------------------------------------------------------------------------------------------------------------------------------------------------------------

def display(im_path):

    dpi = 80
    im_data = plt.imread(im_path)
    height, width, depth = im_data.shape

    # What size does the figure need to be in inches to fit the image?
    figsize = width / float(dpi), height / float(dpi)

    # Create a figure of the right size with one axes that takes up the full figure
    fig = plt.figure(figsize=figsize)
    ax = fig.add_axes([0, 0, 1, 1])

    # Hide spines, ticks, etc.
    ax.axis('off')

    # Display the image.
    ax.imshow(im_data, cmap='gray')

    plt.show()

#------------------------------------------------------------------------------------------------------------------------------------------------------------

def grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#------------------------------------------------------------------------------------------------------------------------------------------------------------

def loading_window():
    # Create the main window
    root = tk.Tk()
    root.title("Loading...")
    
    # Set the size of the window and remove the default window title bar
    root.geometry("400x150")
    root.config(bg="#2e3b4e")  # Dark blue background
    root.resizable(False, False)  # Make the window non-resizable

    # Create a stylish label with a message
    label = tk.Label(root, text="Extracting Text from the Image...", font=("Arial", 14, "bold"), fg="white", bg="#2e3b4e")
    label.pack(pady=20)

    # Create a progress bar
    progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="indeterminate")
    progress.pack(pady=10)
    
    # Start the progress bar animation
    progress.start()

    # Set the window to close after 5 seconds
    root.after(6000, root.destroy)

    # Start the Tkinter event loop
    root.mainloop()
    

#------------------------------------------------------------------------------------------------------------------------------------------------------------
    
# Function to create a dialog box and save text to DOCX
def open_text_dialog_and_save(text):
    # Function to save text to a new DOCX file
    def save_to_docx(text):
        # Ask the user to select a location to save the DOCX file
        file_path = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word Document", "*.docx")])
        
        if file_path:
            try:
                # Create a new Document object
                doc = Document()
                # Add the provided text to the document
                doc.add_paragraph(text)
                # Save the document
                doc.save(file_path)
                messagebox.showinfo("Success", "File saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file: {e}")

    # Function to exit the application
    def exit_app():
        root.quit()

    # Create the main window (root)
    root = tk.Tk()
    root.title("Text Display and Save")

    # Create a Text widget to display and modify text
    text_widget = tk.Text(root, height=10, width=50)
    text_widget.pack(pady=10)

    # Insert some sample text into the Text widget
    text_widget.insert(tk.END, text)

    # Create the Save button
    save_button = tk.Button(root, text="Save to DOCX", command=lambda: save_to_docx(text_widget.get("1.0", tk.END)))
    save_button.pack(side=tk.LEFT, padx=10, pady=10)

    # Create the Exit button
    exit_button = tk.Button(root, text="Exit", command=root.destroy)
    exit_button.pack(side=tk.RIGHT, padx=10, pady=10)

    # Run the Tkinter event loop
    root.mainloop()    

#------------------------------------------------------------------------------------------------------------------------------------------------------------
root = tk.Tk()
root.title("Image Upload")

# Hide the main window (we only want the file dialog)
root.withdraw()

# Call the upload function to open the file dialog
upload_image()

# Close the application after the image is processed or failed
root.destroy()

image_file = "process.jpg"
image = cv2.imread(image_file)

gray = grayscale(image)
cv2.imwrite("C:/Users/admin/Desktop/PROJECT/FINAL/gray.jpg", gray)
grayimg = cv2.imread("C:/Users/admin/Desktop/PROJECT/FINAL/gray.jpg")


thres, im_bw = cv2.threshold(grayimg,120, 255, cv2.THRESH_BINARY)
cv2.imwrite("C:/Users/admin/Desktop/PROJECT/FINAL/binary.jpg", im_bw)
binaryimg = cv2.imread("C:/Users/admin/Desktop/PROJECT/FINAL/binary.jpg")
loading_window()
#display("C:/Users/admin/Desktop/PROJECT/temp/binary.jpg")
# Custom configuration to improve math symbol recognition
custom_config = r'--oem 3 --psm 6'  # Use LSTM OCR engine and block of text mode
ocr = pytesseract.image_to_string(binaryimg, config = custom_config)
#print(ocr)
open_text_dialog_and_save(ocr)


