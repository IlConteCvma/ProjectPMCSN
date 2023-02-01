from enum import Enum

START =        0.0              # initial time                   */
STOP  =    20000.0              # terminal (close the door) time */
INFINITY =  (100.0 * STOP)      # must be much larger than STOP  */

class Timer:
    def __init__(self) -> None:
        self.current        = START         # Current time   
        self.arrival        = INFINITY      # Next Arrival time
        self.completation   = INFINITY      # Next Completation time
    
    def UpdateCurrent(self,val):
        self.current = val


class EventType(Enum):
    ARRIVAL         = 0
    COMPLETATION    = 1


class Event:
    def __init__(self,typ:EventType,id) -> None:
        self.time = INFINITY    # Next occurence of an event
        self.typ = typ          # Event type
        self.client = None      # Client TODO seve o no?
        self.identifier = id    # Identifier of set and server if completation TODO serve?? 




# statistics for population
class Area:
    def __init__(self,nQueue) -> None:
        self.node       = [0.0] * nQueue 
        self.queue      = [0.0] * nQueue
        self.service    = [0.0] * nQueue
    
    def UpdateArea(self,globalTime,current,number):
        self.node    += (globalTime - current) * number
        self.queue   += (globalTime - current) * (number - 1)
        self.service += (globalTime - current)