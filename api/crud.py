def update_state(increase: bool, state:int):
    checkpoint=False
    if increase:
        if state >= 0:
            state += 1

        elif state < 0:
            state = 0

    else:
        if state >= 5:
            state = 0
            checkpoint=True

        elif state > 0:
            state = 0
        
        elif state <= 0:
            state -= 1


    return state, checkpoint

def update_state_ghost(state, ghost_level,speed_level, race_speed):
    if state >= 5:
        if ghost_level != 1 or race_speed < speed_level:
            state = 0

        return state

    if race_speed >= speed_level:
        if ghost_level == 1:
            speed += min((race_speed - speed_level)+1, 3)
        elif ghost_level == 2:
            speed += min((race_speed - speed_level)+1, 2)
        elif ghost_level == 3:
            speed += min((race_speed - speed_level)+1, 1)

    return state

    
def update_speed(speed: int, state: int):
    if state >= 10:
        speed += 1
        state = 0

    elif state < -2:
        speed -= 1
        state = 0

    return speed, state