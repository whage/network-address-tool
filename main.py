#!/usr/bin/python3
import argparse

# TODO __name__ ?
if __name__ == '__main__':
    title = 'A tiny command line utility for querying IP addresses of the host machine.'
    parser = argparse.ArgumentParser(description = title)

    parser.add_argument(
        '--with-prefix',
        help = 'Print addressess with CIDR notation',
        action = 'store_true'
    )

    parser.add_argument(
        '--overlapping',
        help = 'List only overlapping subnets',
        action = 'store_true'
    )

    args = parser.parse_args()