from pioneer_sdk import Camera, Pioneer
import cv2

camera = Camera()
pioneer_mini = Pioneer(logger=False)

aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
aruco_params = cv2.aruco.DetectorParameters()
aruco_detector = cv2.aruco.ArucoDetector(aruco_dict, aruco_params)

while True:
    frame = camera.get_cv_frame()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    corners, ids, rejected = aruco_detector.detectMarkers(gray)
    cv2.aruco.drawDetectedMarkers(frame, corners, ids)
    if ids is not None:
        pioneer_mini.arm()
    else: 
        pioneer_mini.disarm()
            
    cv2.imshow("video", frame)
    cv2.imshow("gray", gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
