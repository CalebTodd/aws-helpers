#!/usr/bin/env python3

import argparse
from functions import set_default_aws_session


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
                        '-p', '--aws_profile',
                        required=True,
                        help="AWS Named Profile to use"
                        )
    args = parser.parse_args()

    set_default_aws_session(args.aws_profile)


if __name__ == '__main__':
    main()
