import os
from services.github import ApiGithub
from models.github import PayloadGithub


def process(key: str, value: dict) -> str:
    """ Create a data product.

        Parameters:
            value (dict): Event value.
    """
    
    try:
        body = PayloadGithub().create_repos_template(data=value)
        ApiGithub().create_repos_template(
            template_owner=os.getenv('GH_TEMPLATE_OWNER', ''),
            template_repo=value.type_dp,
            body=body
        )
        print('Data product created')
        return 'Data product created'

    except Exception as e:
        print(e)
        return f'Error: {e}'
