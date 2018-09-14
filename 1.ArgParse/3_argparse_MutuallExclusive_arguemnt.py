import argparse

"""
	only one at  a time will work
	1. we are keeping the positional arugement
"""

parser = argparse.ArgumentParser()
parser.add_argument("num", help="compulsary argument", type=int)

# create a group

group = parser.add_mutually_exclusive_group()
group.add_argument("-d", "--detailed", help="Detailed explaintion", action="store_true")
group.add_argument("-s", "--short", help="Short explaintion", action="store_true")

args = parser.parse_args()

if args.detailed == True:
	print ("Pring detailed explaintion")
elif args.short == True:
	print ("Only short explaintion required")
else:
	print("Both are not set")