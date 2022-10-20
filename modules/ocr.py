from PIL import Image
import pytesseract
import numpy as np
from io import BytesIO

def image_to_string(file):
    img = Image.open(file)
    return pytesseract.image_to_string(img)
