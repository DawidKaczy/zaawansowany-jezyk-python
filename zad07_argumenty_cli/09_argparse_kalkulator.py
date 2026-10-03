import argparse

parser = argparse.ArgumentParser()

parser.add_argument("a", type=float)

parser.add_argument("b", type=float)

parser.add_argument("--op", choices=['+', '-', '*', '/'], default='+')

args = parser.parse_args()

if args.op == '+':
    print(args.a + args.b)

elif args.op == '-':
    print(args.a - args.b)

elif args.op == '*':
    print(args.a * args.b)

elif args.op == '/':
    print(args.a / args.b)
