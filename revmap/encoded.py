from urllib.parse import quote
from base64 import b64encode
import binascii


class Encode:
    def __init__(self, payload: str):
        self.__payload = payload

    def shell(self):
        return self.__payload

    def urlencode(self):
        return quote(self.__payload)

    def base64(self):
        messagebytes = bytes(self.__payload, 'utf-8')
        return b64encode(messagebytes)

    def hexadecimal(self):
        messagebytes = bytes(self.__payload, 'utf-8')
        return binascii.hexlify(messagebytes)
