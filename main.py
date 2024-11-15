from utils import Utils
import argparse


def main():
    try:
        # Initialize the Utils class (loads config)
        utils = Utils()

        # # Get the start position from the user
        # start_x, start_y = map(int, input("Enter the start position (x y) separated by space: ").split())
        # start = (start_x, start_y)

        # # Get the end position from the user
        # end_x, end_y = map(int, input("Enter the end position (x y) separated by space: ").split())
        # end = (end_x, end_y)

        # # Validate inputs
        # if not (utils.is_within_bounds(start_x, start_y) and utils.is_within_bounds(end_x, end_y)):
        #     print("Error: Start or end position is out of bounds. Please enter values between 0 and 7.")
        #     return

        parser = argparse.ArgumentParser()
        parser.add_argument("start", help="Start position (x y)", type=str)
        parser.add_argument("end", help="End position (x y)", type=str)

        args = parser.parse_args()

        start = tuple(map(int, args.start.split()))
        end = tuple(map(int, args.end.split()))


        # Find all shortest paths
        all_paths = utils.bfs_knight_paths(start, end)
        print("\nAll shortest paths:")
        for path in all_paths:
            print(path)

        # Create Graphviz DOT file
        utils.create_graphviz(all_paths)

    except ValueError:
        print("Invalid input. Please enter two integers separated by a space.")

if __name__ == "__main__":
    main()
