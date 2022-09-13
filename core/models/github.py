

class PayloadGithub:

    def create_repos_template(self, data: dict) -> dict:
        body = {
            'owner': data.owner,
            'name': data.name.strip().replace(' ', '_'), # required
            'include_all_branches': True, # Padrão: false
            'private': True # Padrão: false
        }

        if data.description:
            body.update({'description': data.description})

        return body
