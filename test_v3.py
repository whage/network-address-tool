import subprocess
import re
import ipaddress

class IfconfigParser:
    def __init__(self, str):
        self.raw_data = str

    def parse_ipv4_addresses(self):
        expression = "inet addr:(\S+).*Mask:(\S+)"
        tuples = re.findall(expression, self.raw_data)

        return [(t[0], t[1], self.mask_to_prefix(t[1])) for t in tuples]

    def mask_to_prefix(self, mask):
        return sum([bin(int(x)).count('1') for x in mask.split('.')])

    def get_addresses(self, with_prefix = False):
        addresses = self.parse_ipv4_addresses()

        results = [a[0] for a in addresses]

        if with_prefix:
            results = [a[0] + '/' + str(a[2]) for a in addresses]

        return results

    def get_overlapping_subnets(self):
        pass

    def overlaps(self, subnet1, subnet2):
        pass


ifconfig_output = subprocess.getoutput(["ifconfig"])
p = IfconfigParser(ifconfig_output)

print("\n".join(p.get_addresses(True)))

# build a list of Networks using the ip_network factory function
networks = [ipaddress.ip_network(addr, False) for addr in p.get_addresses(True)]
networks.sort(key = lambda n: n.network_address)

print([n.network_address for n in networks])