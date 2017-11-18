import itertools
import ipaddress

class SubnetManager:
    def get_addresses(self, address_tuples, with_prefix = False):
        results = [a[0] for a in address_tuples]

        if with_prefix:
            results = [a[0] + '/' + str((a[1])) for a in address_tuples]

        return results

    # returns a list of sets where each set contains overlapping pairs of subnets
    def get_overlapping_subnets(self, address_tuples):
        # build a list of Networks using the ip_network factory function
        addresses = self.get_addresses(address_tuples, True)
        overlapping_subnets = []

        # build all posible 2-tuples of networks
        for a1, a2 in itertools.combinations(addresses, 2):
            n1 = ipaddress.ip_network(a1, False)
            n2 = ipaddress.ip_network(a2, False)

            if (n1.overlaps(n2)):
                overlapping_subnets.append({a1, a2})

        return overlapping_subnets
