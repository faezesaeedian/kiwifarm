from utils import Utils
import argparse


def main():
    try:
        # Initialize the Utils class (loads config)
        utils = Utils()

        parser = argparse.ArgumentParser()
        parser.add_argument("start", help="Start position (x y)", type=str)
        parser.add_argument("end", help="End position (x y)", type=str)

        args = parser.parse_args()

        start = tuple(map(int, args.start.split()))
        end = tuple(map(int, args.end.split()))


        # Find all shortest paths
        all_paths = utils.bfs_knight_paths(start, end)
        utils.plot_knight_paths(all_paths)
        
        print("\nAll shortest paths:")
        for path in all_paths:
            print(path)

        # Create Graphviz DOT file
        utils.create_graphviz(all_paths)

    except ValueError:
        print("Invalid input. Please enter two integers separated by a space.")

if __name__ == "__main__":
    main()
