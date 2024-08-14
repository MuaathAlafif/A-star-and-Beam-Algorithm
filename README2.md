# A* Search Algorithm with Temperature Map

This repository contains an implementation of the A* search algorithm that incorporates a temperature map. The temperature map affects the traversal cost of each node, providing a more realistic model where environmental factors like temperature or terrain difficulty are considered.

## Files

- `A_star_search.ipynb`: A Jupyter Notebook that demonstrates the A* search algorithm with a temperature map.
- `A_star_search.py`: The original Python script containing the implementation.

## How to Run

To run the notebook:

1. Clone the repository or download the files.
2. Open `A_star_search.ipynb` in Jupyter Notebook or JupyterLab.
3. Run the cells sequentially to see the algorithm in action.

To run the Python script directly:

1. Ensure you have Python installed.
2. Run the script using the following command:
   ```bash
   python A_star_search.py
   ```

## Example

In the provided example, a 2D grid graph is used with specified temperatures. The algorithm finds the shortest path from the start node `(0, 0)` to the goal node `(1, 2)` considering the additional costs introduced by the temperature map.

## License

This project is licensed under the MIT License.
