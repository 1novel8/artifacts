from character.api.urls import url_mapping as character_url_mapping

urls_mapping = character_url_mapping


def get_url(url_name: str, **kwargs) -> str:
    try:
        endpoint = urls_mapping[url_name]
        if endpoint['params'] != set(kwargs.keys()):
            raise ValueError
        prepared_url = prepare_url(endpoint=urls_mapping[url_name], params=kwargs)
        return prepared_url
    except Exception:
        raise


def prepare_url(endpoint: dict[str, dict], params: dict | None = None) -> str:
    url_pattern = endpoint['url_pattern']
    for param_name in endpoint['params']:
        url_pattern = url_pattern.replace(f'[{param_name}]', params[param_name])
    return url_pattern
