from prompt_toolkit.validation import Validator, ValidationError

class YesNoValidator(Validator):

    def validate(self, document) -> None:
        text = document.text.strip().lower()
        if text not in ['yes', 'no']:
            raise ValidationError(message='Invalid response. Please enter \'yes\' or \'no\'.', cursor_position=len(document.text))

class RequiredValidator(Validator):

    def __init__(self,payloads) -> None:
        self.__payloads = payloads

    def validate(self, document) -> None:
        text = document.text.strip()
        if text not in self.__payloads:
            raise ValidationError(message='Input is required', cursor_position=0)

class RequiredValidatorEncoding(Validator):
    
    def __init__(self,payloads) -> None:
        self.__payloads = payloads

    def validate(self, document) -> None:
        text = document.text.strip()
        if text not in self.__payloads:
            raise ValidationError(message='Encoding is required', cursor_position=0)
