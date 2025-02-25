from PIL import Image
import pytesseract

def extract_text(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

if __name__ == "__main__":
    image_path = input("Enter the path to the image: ")
    extracted_text = extract_text(image_path)
    print("Extracted Text:\n", extracted_text)
