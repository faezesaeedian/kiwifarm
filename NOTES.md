# Knight Moves Project Notes

This document provides detailed notes and documentation for the project, including information on chess notation, classes, code documentation, command-line parameters, configuration files, additional files, Docker setup, error handling, linting, and logging.

## **1. Algebraic (Chess) Notation**
-  Board Representation: The chessboard is modeled as an 8x8 grid with positions represented as (x, y) tuples.
-  Start and End Positions: Input positions are given as integers (e.g., 2 1 for row 2, column 1).
-  Knight Moves: The knight’s possible moves are defined as relative tuples such as (2, 1), (2, -1), etc., loaded from the config.jsonc file.


## **2. Classes**
**`Utils Class**:
The main utility class that provides various methods to:
- Load configurations from a JSONC file.
- Validate positions on the chessboard.
- Implement BFS (Breadth-First Search) to find the shortest paths for a knight from the start to the end position.
- Visualize paths as images using Matplotlib.
- Generate Graphviz .dot files to represent the knight’s movement graph.


## **3. Extra Files**
- Generated Images:
Paths visualized as PNG images using Matplotlib are saved in the output/ directory (e.g., knight_path_1.png).
- Graphviz Files:
A DOT graph is generated, showing the knight’s shortest paths.

## **4. Docker Usage**
The project includes a Dockerfile for containerizing the application.
Steps to Build and Run
1. Build the Docker Image:
 ```python
docker build -t knight-problem .
```
2. Run the Container:
```python
docker run --rm --name knight-container -v $(pwd)/output:/app/output knight-problem python main.py "0 0" "7 7"
```
- --rm: Automatically removes the container after it exits.
- --name: Names the container for easy identification.
- -v $(pwd)/output:/app/output: Mounts the local output/ directory to /app/output in the container, allowing output files to persist locally.


## 5. Error/Exception Handling

The project includes robust error handling:

### Input Validation
- Ensures that the start and end positions are valid integers.

**Example**:
```python
try:
    start = tuple(map(int, args.start.split()))
    end = tuple(map(int, args.end.split()))
except ValueError:
    print("Invalid input. Please enter two integers separated by a space.")
```

## 6. Config File (JSONC Format)

The project uses a configuration file (`config.jsonc`) to define knight moves and other settings:

**Example**:
```jsonc
{
    "roles": {
        "knight_moves": [
            [2, 1], [2, -1], [-2, 1], [-2, -1],
            [1, 2], [1, -2], [-1, 2], [-1, -2]
        ]
    }
}

