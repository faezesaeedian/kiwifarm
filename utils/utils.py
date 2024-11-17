import graphviz
import json
import matplotlib.pyplot as plt
import numpy as np

class Utils:
    
    def __init__(self) -> None:
        """Initialize the Utils class and load configuration from a file."""
        with open('config.json', 'r') as config_file:
            self.config = json.load(config_file)

    @staticmethod
    def is_within_bounds(x, y):
        """Check if a position is within the chessboard boundaries."""
        return 0 <= x < 8 and 0 <= y < 8
    
    def plot_knight_paths(paths):
        for idx, path in enumerate(paths):
            # Create an 8x8 grid
            board = np.zeros((8, 8))

            # Mark each move on the board with an arrow
            plt.figure(figsize=(6, 6))
            plt.imshow(board, cmap="gray", extent=(0, 8, 0, 8))
            plt.gca().invert_yaxis()

            for i in range(len(path) - 1):
                start = path[i]
                end = path[i + 1]
                plt.plot([start[1] + 0.5, end[1] + 0.5], [start[0] + 0.5, end[0] + 0.5],
                            marker="o", color="blue", linestyle="-", linewidth=2)

            # Add labels for each position
            for pos in path:
                plt.text(pos[1] + 0.3, pos[0] + 0.7, f"{pos}", color="red", fontsize=12)

            plt.title(f"Path {idx + 1}")
            plt.grid(True)
            plt.xticks(range(9))
            plt.yticks(range(9))
            plt.show()

    def bfs_knight_paths(self, start, end):
        """Find all minimum-length paths for a knight to move from start to end."""
        queue = [(start, [start])]  
        min_steps = float('inf')
        all_paths = []
        visited = set()

        while queue:
            (x, y), path = queue.pop(0) 

            if len(path) > min_steps:
                break

            if (x, y) == end:
                if len(path) < min_steps:
                    min_steps = len(path)
                    all_paths = [path]
                elif len(path) == min_steps:
                    all_paths.append(path)
                continue

            visited.add((x, y))

            for dx, dy in self.config['roles']['knight_moves']:
                nx, ny = x + dx, y + dy
                if self.is_within_bounds(nx, ny) and (nx, ny) not in visited:
                    queue.append(((nx, ny), path + [(nx, ny)]))

        return all_paths

    @staticmethod
    # def create_graphviz(paths, filename="knight_paths.dot"):
    #     """Create a Graphviz DOT file for visualizing paths."""
    #     dot = graphviz.Digraph(comment="Knight's Shortest Paths")
        
    #     # Add edges for each path
    #     for path in paths:
    #         for i in range(len(path) - 1):
    #             dot.edge(str(path[i]), str(path[i + 1]))
        
    #     # Save to a DOT file
    #     dot.render(filename, format="dot", cleanup=True)
    #     print(f"DOT file saved as {filename}")


    def create_graphviz(paths, filename="output/knight_paths"):
        """Create a Graphviz graph and export it in multiple formats."""

        dot = graphviz.Digraph(comment="Knight's Shortest Paths", format="pdf")

        # Add edges for each path
        for path in paths:
            for i in range(len(path) - 1):
                dot.edge(str(path[i]), str(path[i + 1]), arrowhead="vee")

        # Render as PNG
        dot.render(filename, format="png", cleanup=True)
        print(f"Graph saved as {filename}.png")

        print(f"Graph saved as {filename}.jpg")
