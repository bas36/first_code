from pioneer_sdk import Camera
import cv2

camera = Camera()
while True:
    frame = camera.get_cv_frame()
    cv2.imshow("video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()