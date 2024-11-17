# About the Project

This project is a chess-based utility for calculating all possible shortest paths for a knight's movement from a given start to an end position on the chessboard. The implementation includes features for pathfinding and visualization.

## Key Features

1. **`Utils` Class**:
   - The `Utils` class is responsible for:
     - Calculating all possible paths using the breadth-first search (BFS) algorithm.
     - Visualizing the paths on a chessboard as saved images.
     - Generating a Graphviz graph to represent the connections between moves.

2. **Input Validation**:
   - The program ensures that user inputs are in the correct format (e.g., like ` 4 5`) and within the valid range of the chessboard.
   - If invalid input is detected, the program prompts the user to modify their input and provides clear feedback on the issue.

3. **Config File**:
   - A configuration file is used to define possible moves for different roles in chess (e.g., knight, queen, rook).
   - This allows flexibility to extend the tool to calculate paths for other roles beyond the knight.

4. **Visualization**:
   - Each path is saved as an image showing the knight’s movement step-by-step on an 8x8 chessboard.
   - A graph is generated using Graphviz to illustrate how nodes (positions) are connected during the pathfinding process.

5. **Web Interface**:
   - The project includes a simple webpage hosted on AWS Lambda to allow users to input start and end positions and view all possible paths dynamically.
   - Try it here: [Knight Moves Webpage](http://kiwi-knight-moves.s3-website-us-east-1.amazonaws.com/).

6. **Dockerized for Portability**:
   - The codebase is fully dockerized to enable easy deployment and execution across different environments without dependency issues.

## How to Run

### Local Execution
1. **Build the Docker Image**:
   ```bash
   docker build -t knight-problem .
   ```

2. **Run the Container**:
   ```bash
   docker run --rm --name knight-container -v $(pwd)/output:/app/output knight-problem python main.py "0 0" "7 7"
   ```

   - Replace `"0 0"` and `"7 7"` with any valid start and end positions in algebraic notation (e.g., `h4`, `c7`).

This project demonstrates a modular and extensible approach to solving the knight’s pathfinding problem, with flexibility for further development and real-world applicability.
