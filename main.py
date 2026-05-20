import cv2
import time
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(detectionCon=0.8, maxHands=1)

cap = cv2.VideoCapture(0)

capture_count = 0

while True:

    success, img = cap.read()

  
    hands, img = detector.findHands(img)

    if hands:

        hand = hands[0]

        fingers = detector.fingersUp(hand)

        if fingers == [0,1,1,0,0]:

            filename = f'capture_{capture_count}.jpg'

            cv2.imwrite(filename, img)
            print("CAPTURE!")

            cv2.putText(
                img,
                "CAPTURE!",
                (50,100),
                cv2.FONT_HERSHEY_SIMPLEX,
                2,
                (0,255,0),
                3
            )

            capture_count += 1
            time.sleep(1)


    cv2.imshow("Hand Gesture Capture", img)

    # 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
