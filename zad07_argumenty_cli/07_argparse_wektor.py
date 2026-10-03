import argparse
parser = argparse.ArgumentParser()
parser.add_argument("x1", type=int)
parser.add_argument("y1", type=int)
parser.add_argument("x2", type=int)
parser.add_argument("y2", type=int)
args = parser.parse_args()
print([args.x2 - args.x1, args.y2 - args.y1])