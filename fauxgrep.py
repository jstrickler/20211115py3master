import fileinput
from argparse import ArgumentParser
import re

#  fauxgrep.py  -i  -n  search_term  file1 ...

parser = ArgumentParser(description="Faux Grep")

parser.add_argument("-i", dest="ignore_case", help="ignore case", action="store_true")
parser.add_argument("-n", dest="show_name", help="display file name", action="store_true")
parser.add_argument("search_term", help="search term")
parser.add_argument("files", nargs="+", help="files to search")

args = parser.parse_args()
print(args)

search_term = re.compile(args.search_term, re.I if args.ignore_case else 0)

# logging.debug(f"searching for {args.search_term}")


for line in fileinput.input(args.files):
    if search_term.search(line):
        if args.show_name:
            print(f"{fileinput.filename()}:", end=' ')
        print(f"{line.rstrip()}")

