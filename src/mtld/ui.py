"""
Minimal CLI UI for running demos and training.
"""
import argparse
from .utils import get_logger

logger = get_logger("ui")

def build_parser():
    parser = argparse.ArgumentParser("mtld")
    parser.add_argument("--mode", choices=["demo", "train", "paraview"], default="demo")
    parser.add_argument("--steps", type=int, default=100)
    return parser

def run_from_cli():
    parser = build_parser()
    args = parser.parse_args()
    logger.info(f"Running mode: {args.mode}")
    return args
