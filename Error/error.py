
import traceback


class TaskNotFoundError(BaseException):
    pass

class ApplicationCrashError(BaseException):
    pass

class TodolistNotFoundError(BaseException):
    pass

class CantChangeDefaultListsError(BaseException):
    pass

class AlreadySetError(BaseException):
    pass