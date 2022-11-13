

import time
import numpy as np
from dataclasses import dataclass, field

import marvinglobal.marvinglobal as mg

###########################################
# cart data classes
###########################################
@dataclass
class FloorOffset:
    floorMaxObstacle:int = 15
    floorMaxAbyss:int = 20
    numRepeatedMeasures = 7
    delayBetweenAnalogReads = 20
    minScanCycleDuration = 80
    finalDockingMoveDistance = 12

class UsSensor:
    def __init__(self, id):
        self.sensorId = id
        self.distance:np.ndarray = np.zeros((mg.NUM_US_DISTANCE_SENSORS), dtype=np.int16)

class SwipingIrSensor:
    def __init__(self, id):
        self.sensorId = id
        self.distance:np.ndarray = np.zeros((mg.NUM_SWIPING_IR_DISTANCE_SENSORS), dtype=np.int16)

class StaticIrSensor:
    def __init__(self, id):
        self.sensorId = id
        self.distance:np.ndarray = np.zeros((mg.NUM_STATIC_IR_DISTANCE_SENSORS), dtype=np.int16)
