import itertools
import ipaddress

from . import util

class SubnetManager:
    def get_addresses(self, address_tuples, with_prefix = False):
        results = [a[0] for a in address_tuples]

        if with_prefix:
            results = [a[0] + '/' + str(util.mask_to_prefix(a[1])) for a in address_tuples]

        return results

    # returns a list of sets where each set contains overlapping pairs
    def get_overlapping_subnets(self, address_tuples):
        # build a list of Networks using the ip_network factory function
        networks = [ipaddress.ip_network(addr, False) for addr in self.get_addresses(address_tuples, True)]
        overlapping_networks = []

        # build all posible 2-tuples of networks
        for n1, n2 in itertools.combinations(networks, 2):
            if (n1.overlaps(n2)):
                overlapping_networks.append({n1, n2})

        return overlapping_networks
