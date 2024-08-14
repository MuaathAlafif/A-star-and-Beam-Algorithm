
# Beam Search Algorithm

This repository contains an implementation of the Beam Search algorithm in Python. Beam Search is a heuristic search algorithm that explores a graph by expanding the most promising nodes in a limited-width beam.

## Files
- **beam_search.py**: Python script containing the implementation of the Beam Search algorithm.
- **beam_search.ipynb**: Jupyter Notebook demonstrating the algorithm with detailed explanations and example usage.
- **README.md**: This file, providing an overview of the project.

## Requirements
No additional Python libraries are required beyond the standard library. The implementation uses `heapq` for managing priority queues.

## How to Run
You can run the algorithm in two ways:
1. **Python Script**: Run `beam_search.py` directly in your terminal or command prompt.
2. **Jupyter Notebook**: Open `beam_search.ipynb` using Jupyter Notebook to see the code with explanations.

## Usage Example
```bash
python beam_search.py
```

This will execute the Beam Search algorithm on the example graph defined in the script.

## Beam Search Overview
Beam Search is a heuristic search algorithm used in pathfinding and AI. It is similar to breadth-first search but with a restricted number of nodes at each level, determined by the `beam_width` parameter. The algorithm keeps track of the best paths found so far and expands them to find a path from the start node to the goal node.

