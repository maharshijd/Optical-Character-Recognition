import pytesseract

def extract_text_from_image(image, custom_config=r'--oem 3 --psm 6'):
    return pytesseract.image_to_string(image, config=custom_config)
