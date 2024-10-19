import cv2
import layoutparser as lp
image = cv2.imread("./uploads/Attendance1.jpg")
image = image[..., ::-1]

# load model
model = lp.PaddleDetectionLayoutModel(config_path="lp://PubLayNet/ppyolov2_r50vd_dcn_365e_publaynet/config",
                                threshold=0.5,
                                label_map={0: "Text", 1: "Title", 2: "List", 3:"Table", 4:"Figure"},
                                enforce_cpu=False,
                                enable_mkldnn=True)
# detect
layout = model.detect(image)

# show result
show_img = lp.draw_box(image, layout, box_width=3, show_element_type=True)
show_img.show()