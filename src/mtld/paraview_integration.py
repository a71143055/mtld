"""
ParaView integration utilities.
This module attempts to import paraview.simple. If not available, it provides
safe fallbacks so the rest of the system can run without ParaView.
"""
from typing import Any, Tuple
from .utils import get_logger

logger = get_logger("paraview_integration")

try:
    from paraview.simple import CreateRenderView, Show, Render, Sphere, Delete
    PVSIMPLE_AVAILABLE = True
    logger.info("paraview.simple available")
except Exception:
    PVSIMPLE_AVAILABLE = False
    logger.warning("paraview.simple not available; ParaView features disabled")

def create_demo_source():
    """
    Create a simple demo source for visualization.
    Returns a handle or a placeholder dict when ParaView is not available.
    """
    if PVSIMPLE_AVAILABLE:
        src = Sphere()
        return src
    else:
        return {"type": "sphere", "radius": 1.0}

def create_render_pipeline(data_source: Any) -> Tuple[Any, Any]:
    """
    Create a minimal render pipeline. If ParaView is not installed, returns placeholders.
    """
    if PVSIMPLE_AVAILABLE:
        view = CreateRenderView()
        rep = Show(data_source, view)
        Render()
        return view, rep
    else:
        logger.info("create_render_pipeline: ParaView not available, returning placeholders")
        return {"view": "placeholder"}, {"rep": "placeholder"}

def cleanup(source):
    if PVSIMPLE_AVAILABLE:
        try:
            Delete(source)
        except Exception:
            logger.exception("Failed to delete ParaView source")
    else:
        logger.info("cleanup: nothing to delete for placeholder")
