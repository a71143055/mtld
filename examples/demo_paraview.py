"""
Standalone example to run ParaView demo pipeline.
This script will attempt to use paraview.simple if available.
"""
from src.mtld.paraview_integration import create_demo_source, create_render_pipeline, cleanup
from src.mtld.utils import get_logger

logger = get_logger("examples.demo_paraview")

def run():
    src = create_demo_source()
    view, rep = create_render_pipeline(src)
    logger.info("ParaView demo executed (or placeholder used).")
    cleanup(src)

if __name__ == "__main__":
    run()
