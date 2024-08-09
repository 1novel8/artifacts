import json

from src.character.dto import CharacterDto
from src.common.client import ArtifactsAPIClient
from src.urls import get_url


def characters__all():
    url = get_url(url_name='characters.list')
    response = ArtifactsAPIClient.request(url=url, method='GET')
    characters = json.loads(response.content)['data']
    return [CharacterDto(**character) for character in characters]
