import math

from common.log_config import get_logger

logger = get_logger(__name__)

def cube_square_root(x: float) -> float:
    x_cubed = x ** 3
    x3_sqrt = math.sqrt(x_cubed)
    logger.info(f"input was {x}, cubed = {x_cubed}, square root of cubed = {x3_sqrt}")
    return x3_sqrt
