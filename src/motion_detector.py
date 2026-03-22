import numpy as np
import config 
from scipy.ndimage import label

class MotionDetector:
    def __init__(self, height, width):
        self.h = height
        self.w = width
        self.grid_h = height // config.GRID_SIZE
        self.grid_w = width // config.GRID_SIZE
    
    def detect(self, events):
        grid = np.zeros((self.grid_h, self.grid_w), dtype=np.int32)
        for x, y, t, polarity in events:
            cell_x = x// config.GRID_SIZE
            cell_y = y//config.GRID_SIZE
            grid[cell_y, cell_x] +=1 
        
        active = grid >= config.MIN_EVENTS_PER_CELL
        labeled, num_features = label(active)
        boxes = []
        for i in range(1, num_features + 1):
            ys, xs = np.where(labeled == i)
            x1 = int(xs.min() * config.GRID_SIZE)
            y1 = int(ys.min() * config.GRID_SIZE)
            x2 = int((xs.max() + 1) * config.GRID_SIZE)
            y2 = int((ys.max() + 1) * config.GRID_SIZE)
            boxes.append((x1, y1, x2, y2))

        return boxes