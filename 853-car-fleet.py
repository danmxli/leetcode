"""
bruh
"""

from typing import List
from collections import deque
import math

def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    # pair positions with speeds and sort by position (furthest to closest)
    cars = sorted(zip(position, speed))
    
    # calculate time to target for each car
    times = [(target - p) / s for p, s in cars]
    
    fleets = 1
    # fastest to slowest times
    for i in range(len(times)-2, -1, -1):
        # if current car takes longer than car ahead, it forms new fleet (because it can't catch up before target)
        if times[i] > times[i+1]:
            fleets += 1
        else:
            # current car would catch up, so it joins fleet ahead
            # update its time to match fleet ahead
            times[i] = times[i+1]
            
    return fleets

print(carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]))
print(carFleet(target = 100, position = [0,2,4], speed = [4,2,1]))