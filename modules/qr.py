import cv2, qrcode
import numpy as np
from pyzbar.pyzbar import decode as pyzbar_decode
from io import BytesIO

def decode(file):
    file_bytes = np.asarray(bytearray(file), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    return pyzbar_decode(img)

def create(text):
    qr = qrcode.QRCode(version=2, box_size=10, border=2)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')

    buffer = BytesIO()
    img.save(buffer, format='png')
    return buffer.getvalue()
