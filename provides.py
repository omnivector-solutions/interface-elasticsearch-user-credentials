from charms.reactive import Endpoint


class ElasticUserProvides(Endpoint):

    def configure(self, username, password):
        """
        Configure the elasticsearch relation by providing:
            - elasticsearch_creds
        """

        for relation in self.relations:
            relation.to_publish.update({
                'username': username,
                'password': password,
            })
