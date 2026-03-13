
from PIL import Image
import numpy as np
import cv2

#allowed image formats
ALLOWED_FORMATS =["JPEG", "JPG", "PNG"]

def validate_image(uploaded_file):
    """Validate whether the uploaded file is a valid image type.
    Returns(True,image)if valid,otherwise(False,error_message)"""

    try:
        image = Image.open(uploaded_file)

        if image.format not in ALLOWED_FORMATS:
            return False, "Unsupported image format.Please upload JPG or PNG."

        return True, image

    except Exception:
        return False, "Invalid image file."

def preprocess_image(image):
    """Convert image to OpenCV format and grayscale"""

    img= np.array(image)
    gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    return img,gray

def check_resolution(image):
    """Check if image resolution is sufficient for analysis"""

    width,height=image.size

    if width<300 or height<300:
        return "LOW"
    else:
        return "GOOD"


def convert_to_cv2(image):
    """Convert PIL image to OpenCV format"""

    return cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)

