import os
import core.services.github.ApiGithub as git
import core.models.github.PayloadGithub as payload


class DataProduct:

    def create(self, value: dict) -> str:
        """ Create a data product.

            Parameters:
                value (dict): Event value.
        """
        
        try:
            body = payload().create_repos_template(data=value)
            repo = git().create_repos_template(
                template_owner=os.getenv('GH_TEMPLATE_OWNER'),
                template_repo=value.type_dp,
                body=body
            )
            print(repo)
            return repo

        except Exception as e:
            print(e)
            return f'Error: {e}'
