from pathlib import Path

from modules.common.log_config import get_logger

logger = get_logger(__name__)

def main():
    logger.info("Hello I'm the engine")
    HERE = Path(__file__).parent
    logger.info(HERE)
    for path in HERE.parent.iterdir():
        print(path)
        print(list(path.iterdir()))

if __name__ == "__main__":
    main()
