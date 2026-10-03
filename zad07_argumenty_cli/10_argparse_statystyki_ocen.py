import argparse
import sys
p = argparse.ArgumentParser()
p.add_argument("oceny", type=float, nargs='*')
p.add_argument("--srednia", action="store_true")
p.add_argument("--min", action="store_true")
p.add_argument("--max", action="store_true")
args = p.parse_args()
if not args.oceny:
   sys.exit(0)
any_flag = args.srednia or args.min or args.max
if not any_flag:
   print(f"Lista ocen: {args.oceny}")
else:
   if args.srednia:
       print(f"Średnia: {sum(args.oceny)/len(args.oceny)}")
   if args.min:
       print(f"Minimum: {min(args.oceny)}")
   if args.max:
       print(f"Maximum: {max(args.oceny)}")