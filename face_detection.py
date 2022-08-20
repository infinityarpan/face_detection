import cv2
import dlib
import argparse
import imutils
# Defining the argument parser
parser = argparse.ArgumentParser(description="Face detection with dlib's HOG")
parser.add_argument("image_path", type=str, help="Type in the path to the image")
parser.add_argument("model_names", nargs='+', type=str, help="Type in the model you want to use HOG or CNN")
args = parser.parse_args()
img = cv2.imread(args.image_path)
# imutils is used to resize the image so that it fits into the screen and also the detection will be faster on smaller images.
# resizing is done by imutils as opencv resize method is lenthy.
resized = imutils.resize(img, width=640)
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
for model in args.model_names:
    if model == "HOG":
        hogdetector = dlib.get_frontal_face_detector()
        faces = hogdetector(gray, 1)
        # Getting the top left and the bottom right points returned by dlib.
        for face in faces:
            x1 = face.left()
            y1 = face.top()
            x2 = face.right()
            y2 = face.bottom()
            print("HOG co-ordinates ",x1,y1,x2,y2)
            cv2.rectangle(resized, (x1,y1), (x2, y2), (0,255,0), 2)
            # The following line is in the form cv2.putText(resized, text, org, font, fontScale, color, thickness, cv2.LINE_AA)
            resized = cv2.putText(resized, "HOG", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2, cv2.LINE_AA)
    elif model == "CNN":
        cnn_face_detector = dlib.cnn_face_detection_model_v1("mmod_human_face_detector.dat")
        faces = cnn_face_detector(gray, 1)
        # Getting the top left and the bottom right points returned by dlib.
        for face in faces:
            x1 = face.rect.left()
            y1 = face.rect.top()
            x2 = face.rect.right()
            y2 = face.rect.bottom()
            print("CNN co-ordinates ",x1,y1,x2,y2)
            cv2.rectangle(resized, (x1,y1), (x2, y2), (0,0,255), 2)
            resized = cv2.putText(resized, "CNN", (50, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)
    else:
        print("Enter a valid input")
cv2.imshow("detected_faces", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
