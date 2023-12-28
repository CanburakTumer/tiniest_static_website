from enum import Enum

class ExitCodes(Enum):
    NO_CHANGE = 10
    MORE_THAN_ONE_META = 11
    META_DID_NOT_MATCH = 12