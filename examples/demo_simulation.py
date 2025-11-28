from src.mtld.main import demo_simulation
from src.mtld.utils import get_logger

logger = get_logger("examples.demo_simulation")

if __name__ == "__main__":
    final = demo_simulation(steps=200)
    logger.info(f"Demo finished. final pose: {final['pose']}")
