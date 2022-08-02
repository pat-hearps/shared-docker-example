from pathlib import Path

from common.log_config import get_logger, show_location

logger = get_logger(__name__)

def main():
    HERE = Path(__file__).parent
    logger.info(f"Hello I'm the ENGINE container, located in {HERE}")
    logger.info(f"My working directory contains:")
    show_location(HERE)

if __name__ == "__main__":
    main()
