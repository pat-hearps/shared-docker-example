from pathlib import Path
from random import randint

from common.log_config import get_logger, show_location
from engine.src.calcs import cube_square_root

logger = get_logger(__name__)

def main():
    HERE = Path(__file__).parent
    logger.info(f"Hello I'm the ENGINE container, located in {HERE}")
    logger.info(f"My working directory contains:")
    # call function imported from separate common module
    show_location(HERE)

    # performing dummy operation with func imported from elsewhere in engine module
    # simply to confirm correct use of import statements
    val = randint(1, 20)
    logger.info(f"Doing math with value={val}")
    cube_square_root(val)

if __name__ == "__main__":
    main()
