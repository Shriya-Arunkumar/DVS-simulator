import numpy as np

class EventSimulator:
    def __init__(self, threshold):
        self.threshold = threshold
        self.prev_log = None
        self.timestamp = 0

    def process_frame(self, frame):
        frame = np.log(frame.astype(np.float32) + 1e-6)
        if self.prev_log is None :
            self.prev_log = frame
            return []
        events =[]
        diff = frame - self.prev_log
        on_mask = diff > self.threshold
        off_mask = diff < -self.threshold

        ys_on, xs_on = np.where(on_mask)
        ys_off, xs_off = np.where(off_mask)

        for xs, ys in zip(xs_on, ys_on):
            events.append((xs, ys, self.timestamp,1))

        for xs, ys in zip(xs_off, ys_off):
            events.append((xs, ys, self.timestamp,-1))
        
        self.prev_log = frame
        self.timestamp += 1
        return events 

