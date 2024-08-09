from src.common.client import ArtifactsAPIClient
from src.urls import get_url


def character__fight(character_name: str) -> None:
    url = get_url(url_name='characters.fight', name=character_name)
    ArtifactsAPIClient.request(url=url, method='POST')


def character__move(character_name: str, x: int, y: int) -> None:
    url = get_url(url_name='characters.move', name=character_name)
    ArtifactsAPIClient.request(url=url, method='POST', data={'x': x, 'y': y})
