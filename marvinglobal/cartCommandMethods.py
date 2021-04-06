
import numpy as np
import marvinglobal.marvinglobal as mg


class CartCommandMethods:

    @staticmethod
    def testSensor(requestQueue, sensorId):
        #print(f"sensor test command added to {requestQueue}")
        requestQueue.put({'sender': config.processName, 'cmd': mg.CartCommands.TEST_IR_SENSOR, 'sensorId': sensorId})

    @staticmethod
    def move(requestQueue, direction:mg.MoveDirection, speed, distance, protected:bool = True):
        requestQueue.put({'sender': config.processName, 'cmd': mg.CartCommands.MOVE, 'direction': direction, 'speed': speed, 'distance': distance, 'protected': protected})

    @staticmethod
    def rotate(requestQueue, relAngle: int, speed):
        requestQueue.put({'sender': config.processName, 'cmd': mg.CartCommands.ROTATE, 'relAngle': relAngle, 'speed': speed})

    @staticmethod
    def setIrSensorReferenceDistances(requestQueue, sensorId:int, distances:np.ndarray):
        requestQueue.put({'sender': config.processName, 'cmd': mg.CartCommands.SET_IR_SENSOR_REFERENCE_DISTANCES, 'sensorId': sensorId, 'distances': distances})

    @staticmethod
    def setVerbose(requestQueue, verbose:bool):
        requestQueue.put({'sender': config.processName, 'cmd': mg.CartCommands.SET_VERBOSE, 'flag': verbose})

    @staticmethod
    def stopCart(requestQueue, reason:str):
        requestQueue.put({'sender': config.processName, 'cmd': mg.CartCommands.STOP_CART, 'reason': reason})
