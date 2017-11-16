import subprocess
import re
import ipaddress
import itertools

class IfconfigParser:
    def __init__(self, str):
        self.raw_data = str

    def parse_ipv4_addresses(self):
        expression = "inet addr:(\S+).*Mask:(\S+)"
        tuples = re.findall(expression, self.raw_data)

        return [(t[0], t[1], self.mask_to_prefix(t[1])) for t in tuples]

    def mask_to_prefix(self, mask):
        return sum([bin(int(x)).count('1') for x in mask.split('.')])

class SubnetManager:
    def pluck_address(self, address_tuples, with_prefix = False):
        results = [a[0] for a in address_tuples]

        if with_prefix:
            results = [a[0] + '/' + str(a[2]) for a in address_tuples]

        return results

    def get_overlapping_subnets(self, networks):
        overlapping_networks = []

        # build all posible 2-tuples of networks
        for n1, n2 in itertools.combinations(networks, 2):
            if (n1.overlaps(n2)):
                overlapping_pairs.add((n1, n2))

        return overlapping_networks


ifconfig_output = subprocess.getoutput(["ifconfig"])
p = IfconfigParser(ifconfig_output)

address_tuples = p.parse_ipv4_addresses()

sm = SubnetManager()

print("\n".join(sm.pluck_address(address_tuples, True)))

# build a list of Networks using the ip_network factory function
networks = [ipaddress.ip_network(addr, False) for addr in sm.pluck_address(address_tuples, True)]

print([n.network_address for n in networks])

print(sm.get_overlapping_subnets(networks))