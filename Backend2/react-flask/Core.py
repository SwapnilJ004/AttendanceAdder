import cv2
import layoutparser as lp
from paddleocr import PaddleOCR, draw_ocr
image = cv2.imread("./uploads/Attendance3.jpg")
image = image[..., ::-1]

# load model
model = lp.PaddleDetectionLayoutModel(config_path="lp://PubLayNet/ppyolov2_r50vd_dcn_365e_publaynet/config",
                                threshold=0.5,
                                label_map={0: "Text", 1: "Title", 2: "List", 3:"Table", 4:"Figure"},
                                enforce_cpu=False,
                                enable_mkldnn=True)
# detect
layout = model.detect(image)

for l in layout:
    if l.type == 'Table':
        x_1 = int(l.block.x_1)
        y_1 = int(l.block.y_1)
        x_2 = int(l.block.x_2)
        y_2 = int(l.block.y_2)
    break

im = cv2.imread("./uploads/Attendance3.jpg")

cv2.imwrite('ext_im.jpg', im[y_1:y_2,x_1:x_2])

ocr = PaddleOCR(lang='en')
image_path = 'ext_im.jpg'
image_cv = cv2.imread(image_path)
image_height = image_cv.shape[0]
image_width = image_cv.shape[1]
output = ocr.ocr(image_path)

print(output)

boxes = [line[0] for line in output]
texts = [line[1][0] for line in output]
probabilities = [line[1][1] for line in output]

image_boxes = image_cv.copy()

for box in boxes:
    top_left_x = int(box[0][0][0])
    top_left_y = int(box[0][0][1])
    bottom_right_x = int(box[0][2][0])
    bottom_right_y = int(box[0][2][1])
    
    # Draw the rectangle
    cv2.rectangle(image_boxes, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 0, 255), 1)


cv2.imwrite('detections.jpg', image_boxes)