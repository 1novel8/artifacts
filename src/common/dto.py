import json
import typing

from pydantic import (AnyHttpUrl, BaseModel, BeforeValidator, ConfigDict,
                      Field, model_validator)

DictResponseData = typing.Annotated[
    dict | list | None, BeforeValidator(lambda _: json.loads(_).get('data'))
]

ErrorResponseMessage = typing.Annotated[
    str | None, BeforeValidator(lambda _: json.loads(_).get('error', {}).get('message'))
]


class BaseDto(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True, frozen=True, from_attributes=True)


class PaginatedDto(BaseDto):
    total: int = None
    page: int = None
    pages: int = None
    size: int = None


class ResponseDto(PaginatedDto):
    data: dict | list | None
    status_code: int = None
    error_message: str | None = None

    @model_validator(mode='before')
    @classmethod
    def parse_response(cls, data: typing.Any) -> typing.Any:
        json_payload = json.loads(data.content)
        return {
            'data': json_payload.get('data'),
            'status_code': data.status_code,
            'error_message': json_payload.get('error', {}).get('message'),
            'total': json_payload.get('total'),
            'page': json_payload.get('page'),
            'pages': json_payload.get('pages'),
            'size': json_payload.get('size'),
        }


class RequestDto(BaseDto):
    url: AnyHttpUrl
    method: int = None
    error_message: ErrorResponseMessage = Field(validation_alias='content')
