

import typing



class LogLevel:
    ERROR : int = 0
    WARNING : int = 1
    DEBUG : int = 2
    INFO : int = 3

class ErrorCode:
    def __init__(self, ec : int):
        self.ec : int = ec

    def __str__(self) -> str:
        if self.ec == 0:
            return "Failure"
        elif self.ec == 1:
            return "Success"
        else:
            return str(self.ec)


def log(val : typing.Any, level : int):
    # if level <= LogLevel.WARNING:
    print(val)