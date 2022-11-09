

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
