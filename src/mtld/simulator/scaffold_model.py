"""
Scaffold model: geometric/structural placeholder representing the 'frame' that
would host tissue in a physical design. This is purely geometric and numeric.
"""
from dataclasses import dataclass
from typing import List
import numpy as np

@dataclass
class Node:
    id: int
    position: List[float]

@dataclass
class Edge:
    a: int
    b: int
    stiffness: float

class ScaffoldModel:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def generate_grid(self, nx=3, ny=3, spacing=1.0):
        self.nodes = []
        self.edges = []
        idx = 0
        for i in range(nx):
            for j in range(ny):
                self.nodes.append(Node(id=idx, position=[i*spacing, j*spacing, 0.0]))
                idx += 1
        # connect grid edges
        for i in range(nx):
            for j in range(ny):
                id0 = i*ny + j
                if j+1 < ny:
                    self.edges.append(Edge(a=id0, b=id0+1, stiffness=1.0))
                if i+1 < nx:
                    self.edges.append(Edge(a=id0, b=id0+ny, stiffness=1.0))

    def to_dict(self):
        return {
            "nodes": [ {"id": n.id, "pos": n.position} for n in self.nodes ],
            "edges": [ {"a": e.a, "b": e.b, "k": e.stiffness} for e in self.edges ]
        }
