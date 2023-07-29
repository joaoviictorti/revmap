import argparse
from argparse import RawTextHelpFormatter
from .utils import Terminal


def banner() -> str:
    return """
 ___ ___ _ _ _____ ___ ___ 
|  _| -_| | |     | .'| . |
|_| |___|\_/|_|_|_|__,|  _|
                      |_|  
        v0.0.8 - @joaoviictorti                          
"""


def argumentos() -> None:
    global args
    parser = argparse.ArgumentParser(
        prog=banner(),
        usage='revmap --ip 192.168.4.80 --port 4444',
        formatter_class=RawTextHelpFormatter,
    )
    parser.add_argument('--version', action='version', version='revmap 0.0.8')
    parser.add_argument(
        '--ip',
        type=str,
        dest='ip',
        action='store',
        help='Insert ip',
        required=True,
    )
    parser.add_argument(
        '--port',
        type=str,
        dest='porta',
        action='store',
        help='Insert port',
        required=True,
    )
    args = parser.parse_args()
    print(banner())
    Terminal(args.ip, args.porta).cli()