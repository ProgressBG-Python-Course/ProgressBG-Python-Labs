import argparse

# Create the parser
parser = argparse.ArgumentParser(
    description="Example script demonstrating argparse usage."
)

# define positional required argument:
parser.add_argument("message", help="the message to be repeated")

# define optional argument:
parser.add_argument(
    "--repeat",
    type=int,
    default=1,
    help="How many times to repeat the message (default: %(default)s)",
)

# Parse arguments
args = parser.parse_args()

# Use arguments
for _ in range(args.repeat):
    print(args.message)
