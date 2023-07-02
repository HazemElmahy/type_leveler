from pydantic import BaseModel


class UpdateSpeed(BaseModel):
    speed: int
    is_ghost: bool = False
    ghost_level: int = 0

class GetSpeedLevel(BaseModel):
    speed: int
    state: int