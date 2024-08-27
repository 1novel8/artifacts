from src.common.dto import ResponseDto


class UnexpectedStatusCode(Exception):
    status_code: int
    message: str

    def __init__(self, response: ResponseDto):
        self.status_code = response.status_code
        self.message = response.error_message

    def __str__(self):
        return f"UnexpectedStatusCode: Status code: {self.status_code}, Message: {self.message}"
