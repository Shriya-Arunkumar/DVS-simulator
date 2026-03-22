import cv2
from src.simulator import EventSimulator
from src.visualizer import Visualizer

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
h, w = frame.shape[:2]

sim = EventSimulator(threshold=0.15)
viz = Visualizer(h, w)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    events = sim.process_frame(gray)
    canvas = viz.update(events)

    cv2.imshow("DVS Simulator", canvas)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()