import cv2
import pytesseract
from PIL import Image
from matplotlib import pyplot as plt
import tkinter as tk
from tkinter import ttk,Toplevel,filedialog,messagebox
import time

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
    
def show_text_in_dialog(text):
    # Assign the text to a variable
    text_to_display = text
    
    # Create the main window (it will not appear)
    root = tk.Tk()
    root.withdraw()  # Hide the main window (since we're just using the dialog)

    # Create a custom top-level window (dialog)
    dialog = Toplevel(root)
    dialog.title("Output")
    
    # Create a label with the text you want to display
    label = tk.Label(dialog, text=text_to_display, padx=50, pady=20)
    label.pack()

    # Create a close button to dismiss the dialog
    close_button = tk.Button(dialog, text="Close", command=root.destroy)
    close_button.pack(pady=10)

    # Prevent the dialog window from resizing
    dialog.resizable(True, True)

    # Center the dialog window on the screen
    dialog.geometry(f"+{root.winfo_screenwidth() // 2 - dialog.winfo_reqwidth() // 2}+{root.winfo_screenheight() // 2 - dialog.winfo_reqheight() // 2}")

    # Run the custom dialog
    dialog.mainloop()
    

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
show_text_in_dialog(ocr)


