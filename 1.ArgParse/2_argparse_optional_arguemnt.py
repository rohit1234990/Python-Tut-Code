import argparse

parser = argparse.ArgumentParser()
parser.add_argument("num", help="compulsary argument", type=int)
parser.add_argument("-o", "--output", help="specified if output to be written to external file", action="store_true")


args = parser.parse_args()

print("User supplied : {}".format(args.num))
if args.output:
	print ("Yes to be written")
else:
	print ("Nothing specified")
