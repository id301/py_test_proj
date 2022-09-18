from enum import Enum

class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = "Received status code is not equal to expected"
    WRONG_ELEMENT_COUNT = "Received number of elements is not equal to expected"
    EXPECTED_FIELD_NOT_EXISTS = "Received body doesnt contain expected field"



