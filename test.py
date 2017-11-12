import subprocess
import re

class Address:
    def __init__(self, address, mask):
        self.address = address
        self.mask = mask

    def get_range(self):
        pass

class IfconfigParser:
    def __init__(self, str):
        self.raw_data = str

    def parse_ipv4_addresses(self):
        # TODO: separate expressions, add expression for ipv6 too
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


ifconfig_output = subprocess.check_output(["ifconfig"])
p = IfconfigParser(ifconfig_output)

print "\n".join(p.get_addresses(True))