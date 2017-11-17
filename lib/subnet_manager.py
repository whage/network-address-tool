import itertools
import ipaddress

from . import util

class SubnetManager:
    def pluck_address(self, address_tuples, with_prefix = False):
        results = [a[0] for a in address_tuples]

        if with_prefix:
            results = [a[0] + '/' + str(util.mask_to_prefix(a[1])) for a in address_tuples]

        return results

    def get_overlapping_subnets(self, address_tuples):
        # build a list of Networks using the ip_network factory function
        networks = [ipaddress.ip_network(addr, False) for addr in self.pluck_address(address_tuples, True)]
        overlapping_networks = []

        # build all posible 2-tuples of networks
        for n1, n2 in itertools.combinations(networks, 2):
            if (n1.overlaps(n2)):
                overlapping_pairs.add((n1, n2))

        return overlapping_networks