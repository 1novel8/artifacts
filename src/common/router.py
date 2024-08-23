import functools
import re
import typing
from copy import copy

from pydantic import BaseModel

from src.common.client import ArtifactsAPIClient
from src.common.dto import ResponseDto


def replace_substrings(text, **kwargs):
    for key, value in kwargs.items():
        text = text.replace('{' + key + '}', value)
    return text


def extract_placeholders(text):
    # Регулярное выражение для поиска текста в фигурных скобках
    pattern = r'\{(\w+)\}'
    # Поиск всех совпадений
    placeholders = re.findall(pattern, text)
    return placeholders


def route(url: str, method: str, request_dto: typing.Type[BaseModel] | None, response_dto: typing.Type[BaseModel] | None):
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(**kwargs):
            nonlocal url, method, request_dto, response_dto
            url_ = copy(url)
            path_params = extract_placeholders(url_)
            if path_params:
                path_params = {
                    path_param: kwargs.pop(path_param) for path_param in path_params
                }
                url_ = replace_substrings(url_, **path_params)

            data = kwargs.get('data')
            if data:
                data = kwargs.pop('data')
                if request_dto:
                    data = request_dto.model_validate(data)
                    data = data.model_dump_json()

            response = await ArtifactsAPIClient().request(url=url_, data=data, method=method, **kwargs)
            response = ResponseDto.model_validate(response)
            if response_dto:
                return response_dto.model_validate(response.data)
            return response

        return wrapper

    return decorator
