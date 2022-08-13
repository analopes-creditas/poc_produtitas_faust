import os
import faust
from dotenv import load_dotenv
from api_github import ApiGitHub


load_dotenv()


class DataProduct(faust.Record, serializer='json'):
    type_dp: str
    owner: str
    name: str
    description: str


app = faust.App('produtitas', broker=os.getenv('KFK_SERVER', ''))
principal_topic = app.topic(os.getenv('KFK_TOPIC_NAME', ''), value_type=DataProduct)


def process(value: dict) -> str:
    """ Create a data product.

        Parameters:
            value (dict): Event value.
    """

    body = {
        'owner': value.owner,
        'name': value.name.strip().replace(' ', '_'), # required
        'description': value.description if value.description else '',
        'include_all_branches': True, # Padrão: false
        'private': True # Padrão: false
    }

    ApiGitHub().create_repos_template(
        template_owner=os.getenv('GH_TEMPLATE_OWNER', ''),
        template_repo=value.type_dp,
        body=body
    )
    print('Data product created')
    return 'Data product created'


@app.agent(principal_topic)
async def processor(events):
    async for event in events:
        process(value=event)


if __name__ == '__main__':
    app.main()
