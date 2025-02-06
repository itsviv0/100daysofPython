# 1. Loop Until Goal is Reached

# 2. The while loop runs as long as the robot has not reached the goal.

# 3. Check If Right is Clear.

# 4. If there’s no obstacle to the right, the robot turns right and moves forward.

# 5. Check If Front is Clear:

# 6. If the robot cannot turn right but can move forward, it does so.

# 7. Turn Left if Blocked:

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()