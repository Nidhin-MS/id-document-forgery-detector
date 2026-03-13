import cv2
import numpy as np
import pytesseract

def analyze_document(image):

    img = np.array(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    laplacian = cv2.Laplacian(gray, cv2.CV_64F).var()
    blur_score = laplacian

    edges = cv2.Canny(gray,100,200)
    edge_score = edges.mean()

    text = pytesseract.image_to_string(gray)

    tamper_flag = False

    if blur_score < 50:
        tamper_flag = True

    return {
        "blur_score": float(blur_score),
        "edge_score": float(edge_score),
        "extracted_text": text[:200],
        "tampering_suspected": tamper_flag
    }