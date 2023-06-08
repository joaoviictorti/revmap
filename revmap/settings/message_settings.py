class Message:

    @staticmethod
    def message_language(ip, porta):
        message = [
            ('class:ip', f'{ip}'),
            ('class:porta', f' ({porta})'),
            ('class:revmap', ' [revmap] # ')
        ]

        return message
    
    @staticmethod
    def message_validation():
        message = [
            ('class:message', 'Do you want to use encoding? '),
            ('class:yes_no', f' (Yes/No)'),
            ('class:revmap', ' [revmap] # ')
        ]

        return message
    
    @staticmethod
    def message_encoding():
        message = [
            ('class:message', 'Insert encode'),
            ('class:revmap', ' [revmap] # ')
        ]

        return message