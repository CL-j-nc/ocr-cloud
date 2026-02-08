from paddleocr import PaddleOCR
import cv2

ocr = PaddleOCR(
    use_angle_cls=False,
    det_limit_side_len=960,
    use_gpu=True
)

def run_ocr(image_path):
    img = cv2.imread(image_path)
    result = ocr.ocr(img, cls=False)
    return [line[1][0] for line in result[0]]
