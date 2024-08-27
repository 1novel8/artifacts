from src.auth.api.schema import AuthSchema, TokenSchema
from src.auth.utils import basic_auth
from src.common import status_code
from src.common.client import ArtifactsAPIClient
from src.common.exception import UnexpectedStatusCode


async def token__get(*, auth: AuthSchema) -> TokenSchema:
    headers = {'Authorization': basic_auth(username=auth.username, password=auth.password)}
    response = await ArtifactsAPIClient().call_api(url='/token', method='POST', headers=headers)

    if response.status_code != status_code.OK:
        raise UnexpectedStatusCode(response)
    return TokenSchema.model_validate(response.data)
