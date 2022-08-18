import os
import services.github.ApiGithub as git
import models.github.PayloadGithub as payload


class DataProductCreate:

    def process(self, key: str, value: dict) -> str:
        """ Create a data product.

            Parameters:
                value (dict): Event value.
        """
        
        try:
            body = payload().create_repos_template(data=value)
            git().create_repos_template(
                template_owner=os.getenv('GH_TEMPLATE_OWNER', ''),
                template_repo=value.type_dp,
                body=body
            )
            print('Data product created')
            return 'Data product created'

        except Exception as e:
            print(e)
            return f'Error: {e}'
