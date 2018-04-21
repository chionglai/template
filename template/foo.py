#!/usr/bin/env python

import sys
import argparse


def main(argv=sys.argv[1:]):
    """Example of exeutable console script.
    """
    parser = argparse.ArgumentParser(description="Process some input argument.")
    parser.add_argument("file1", metavar="file_1", type=str, nargs=1,
                        help="Path to file 1")
    parser.add_argument("--file2", dest="file2", action="store",
                        default=None, help="Path to file 2")
    parser.add_argument("integers", metavar="N", type=int, nargs="+",
                        help="an integer for the accumulator")
    parser.add_argument("--sum", dest="accumulate", action="store_const",
                        const=sum, default=max,
                        help="sum the integers (default: find the max)")

    args = parser.parse_args(argv)
    print(args.accumulate(args.integers))
    print(args.file1)
    print(args.file2)


if __name__ == "__main__":
    main()
