import argparse
from argparse import RawTextHelpFormatter
from .payloads import *


def banner():
    return """
 ___ ___ _ _ _____ ___ ___ 
|  _| -_| | |     | .'| . |
|_| |___|\_/|_|_|_|__,|  _|
                      |_|  
        v0.0.1 - @joaoviictorti                          
"""


def argumentos():
    global args
    parser = argparse.ArgumentParser(
        prog=banner(),
        usage='revmap --ip 192.168.4.80 --port 4444 --payload bash --encode urlencode',
        formatter_class=RawTextHelpFormatter,
    )
    parser.add_argument('--version', action='version', version='revmap 0.0.1')
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
    parser.add_argument(
        '--payload',
        type=str,
        dest='payload',
        action='store',
        choices=[
            'bash',
            'python',
            'powershell',
            'nc',
            'php',
            'perl',
            'ruby',
            'telnet',
            'nodejs',
            'golang',
        ],
        help='Insert payload',
        required=True,
    )
    parser.add_argument(
        '--encode',
        type=str,
        dest='encode',
        action='store',
        choices=['base64', 'hexadecimal', 'urlencode', 'shell'],
        help='Insert encode',
        required=True,
    )
    args = parser.parse_args()

    match args.payload:
        case 'bash':
            match args.encode:
                case 'urlencode' | 'hexadecimal' | 'base64' | 'shell':
                    print(
                        eval(
                            f'Bash("{args.ip}","{args.porta}").{args.encode}()'
                        )
                    )
        case 'python':
            match args.encode:
                case 'urlencode' | 'hexadecimal' | 'base64' | 'shell':
                    print(
                        eval(
                            f'Python("{args.ip}","{args.porta}").{args.encode}()'
                        )
                    )
        case 'powershell':
            match args.encode:
                case 'urlencode' | 'hexadecimal' | 'base64' | 'shell':
                    print(
                        eval(
                            f'Powershell("{args.ip}","{args.porta}").{args.encode}()'
                        )
                    )
        case 'nc':
            match args.encode:
                case 'urlencode' | 'hexadecimal' | 'base64' | 'shell':
                    print(
                        eval(
                            f'Netcat("{args.ip}","{args.porta}").{args.encode}()'
                        )
                    )
        case 'perl':
            match args.encode:
                case 'urlencode' | 'hexadecimal' | 'base64' | 'shell':
                    print(
                        eval(
                            f'Perl("{args.ip}","{args.porta}").{args.encode}()'
                        )
                    )
        case 'php':
            match args.encode:
                case 'urlencode' | 'hexadecimal' | 'base64' | 'shell':
                    print(
                        eval(
                            f'PHP("{args.ip}","{args.porta}").{args.encode}()'
                        )
                    )
        case 'ruby':
            match args.encode:
                case 'urlencode' | 'hexadecimal' | 'base64' | 'shell':
                    print(
                        eval(
                            f'Ruby("{args.ip}","{args.porta}").{args.encode}()'
                        )
                    )
        case 'telnet':
            match args.encode:
                case 'urlencode' | 'hexadecimal' | 'base64' | 'shell':
                    print(
                        eval(
                            f'Telnet("{args.ip}","{args.porta}").{args.encode}()'
                        )
                    )
        case 'nodejs':
            match args.encode:
                case 'urlencode' | 'hexadecimal' | 'base64' | 'shell':
                    print(
                        eval(
                            f'NodeJs("{args.ip}","{args.porta}").{args.encode}()'
                        )
                    )
        case 'golang':
            match args.encode:
                case 'urlencode' | 'hexadecimal' | 'base64' | 'shell':
                    print(
                        eval(
                            f'Golang ("{args.ip}","{args.porta}").{args.encode}()'
                        )
                    )
