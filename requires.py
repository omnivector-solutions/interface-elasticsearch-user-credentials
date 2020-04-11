from charms.reactive import when
from charms.reactive import set_flag, clear_flag
from charms.reactive import Endpoint


class ElasticUserRequires(Endpoint):

    @when('endpoint.{endpoint_name}.joined')
    def joined(self):
        if any(unit.received['password'] for unit in self.all_joined_units):
            set_flag(self.expand_name('available'))

    @when('endpoint.{endpoint_name}.changed')
    def changed(self):
        if any(unit.received['password'] for unit in self.all_joined_units):
            set_flag(self.expand_name('available'))

    def list_unit_data(self):
        """
        Get the list of the relation info for each unit.

        Returns a list of dicts, where each dict contains the elasticsearch
        cluster name, the host (address) and the port (as a string).
        For example::
            [
                {
                    'username': 'elastic',
                    'password': '9382ldewrude98soi',
                },
            ]
        """
        units_data = []
        for relation in self.relations:
            for unit in relation.joined_units:
                username = unit.received['username']
                password = unit.received['password']
                if not (username and password):
                    continue
                units_data.append({
                    'username': username,
                    'password': password,
                })
        return units_data
