from prompt_toolkit.styles import Style

class Color:

    @staticmethod
    def language() -> list:
        style_language = Style.from_dict({
            'ip': '#0000FF',
            'porta': '#00aa00',
            'revmap': '#884444',
        })
        
        return style_language
    
    @staticmethod
    def validation() -> list:
        style_validation  = Style.from_dict({
            'message': '#884444',
            'yes_no': '#00aa00',
            'revmap': '#884444',
        })

        return style_validation

    @staticmethod
    def encoding() -> list:
        style_encoding = Style.from_dict({
            'message': '#884444',
            'revmap': '#884444',
        })

        return style_encoding