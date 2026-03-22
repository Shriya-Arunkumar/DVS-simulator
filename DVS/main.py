import cv2
import config
from src.simulator import EventSimulator
from src.visualizer import Visualizer
from src.motion_detector import MotionDetector

cap = cv2.VideoCapture(0)

ret, frame = cap.read()
h, w = frame.shape[:2]

sim = EventSimulator(threshold=0.15)
viz = Visualizer(h, w)
det = MotionDetector(h, w)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    events = sim.process_frame(gray)
    canvas = viz.update(events)
    boxes = det.detect(events)
    for x1, y1, x2, y2 in boxes:
        cv2.rectangle(canvas, (x1, y1), (x2, y2), (0, 255, 0), 1)    
    
    cv2.imshow("DVS Simulator", canvas)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break   

cap.release()
cv2.destroyAllWindows()
