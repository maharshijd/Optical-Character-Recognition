import cv2
from file_handling import upload_image, save_image
from image_processing import grayscale, threshold_image
from ocr_processing import extract_text_from_image
from gui import show_loading_window, display_text_in_gui
from PIL import Image

def main():
    file_path = upload_image()
    if not file_path:
        print("No image selected.")
        return
    
    image = cv2.imread(file_path)
    gray_img = grayscale(image)
    binary_img = threshold_image(gray_img)

    save_image(Image.fromarray(binary_img), "processed_image.jpg")

    show_loading_window()

    ocr_text = extract_text_from_image(binary_img)

    display_text_in_gui(ocr_text)

if __name__ == "__main__":
    main()
