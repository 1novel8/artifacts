import json
import typing

from pydantic import BaseModel, ConfigDict, Field, BeforeValidator, AnyHttpUrl

DictResponseData = typing.Annotated[
    dict | list | None, BeforeValidator(lambda _: json.loads(_).get('data'))
]

ErrorResponseMessage = typing.Annotated[
    str | None, BeforeValidator(lambda _: json.loads(_).get('error', {}).get('message'))
]


class BaseDto(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True, frozen=True, from_attributes=True)


class ResponseDto(BaseDto):
    data: DictResponseData = Field(validation_alias='content')
    status_code: int = None
    error_message: ErrorResponseMessage = Field(validation_alias='content')


class RequestDto(BaseDto):
    url: AnyHttpUrl
    method: int = None
    error_message: ErrorResponseMessage = Field(validation_alias='content')
