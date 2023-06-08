from prompt_toolkit.completion import WordCompleter
from .validator_required import RequiredValidator, YesNoValidator, RequiredValidatorEncoding
from ..settings import *
from .generator_payloads import revershell_generator
from prompt_toolkit import PromptSession
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from ..events import bindings

class Terminal():
    def __init__(self, ip: str, porta: str) -> None:

        self.__language_completer = WordCompleter(LANGUAGE_COMPLETER)

        self.__encoding_completer = WordCompleter(ENCODING_COMPLETER)

        self.__socket = [ip,porta]

    def cli(self) -> None:

        session = PromptSession()
        print("[tab] for commands suggestions")
        while True:
            language = session.prompt(
                message=Message.message_language(self.__socket[0], self.__socket[1]),
                style=Color.language(),
                completer=self.__language_completer, 
                validator=RequiredValidator(LANGUAGE_COMPLETER), 
                validate_while_typing=True,
                auto_suggest=AutoSuggestFromHistory(),
                key_bindings=bindings
            )

            validation = session.prompt(
                message=Message.message_validation(), 
                style=Color.validation(),
                validator=YesNoValidator(), 
                validate_while_typing=True,
                auto_suggest=AutoSuggestFromHistory()
            )

            match validation:
                case "yes":
                    encoding = session.prompt(
                        message=Message.message_encoding(), 
                        style=Color.encoding(), 
                        completer=self.__encoding_completer,
                        validator=RequiredValidatorEncoding(ENCODING_COMPLETER), 
                        validate_while_typing=True,
                        auto_suggest=AutoSuggestFromHistory()
                    )
                    revershell_generator(language, encoding,self.__socket[0],self.__socket[1])
                case _:
                    revershell_generator(language,"shell", self.__socket[0],self.__socket[1])