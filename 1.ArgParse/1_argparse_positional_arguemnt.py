import argparse

parser = argparse.ArgumentParser()
parser.add_argument("num", help="compulsary argument", type=int)
args = parser.parse_args()

print("User supplied : {}".format(args.num))
