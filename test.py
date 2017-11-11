import subprocess
import re

class NetworkManager:
    def ifconfig(self):
        return subprocess.check_output(["ifconfig"])

class IPAddressParser:
    def __init__(self, str):
        self.raw_data = str

    def parse_ipv4_addresses(self):
        tuples = self.parse_address_mask_tuples()

        return self.extend_with_prefix(tuples)

    def extend_with_prefix(self, tuples):
        results = []

        for tuple in tuples:
            results.append((tuple[0], tuple[1], self.get_prefix(tuple[1])))

        return results

    def get_prefix(self, mask):
        prefix = sum([bin(int(x)).count('1') for x in mask.split('.')])
        return prefix

    def parse_address_mask_tuples(self):
        expression = "inet addr:(\S+).*Mask:(\S+)"
        return re.findall(expression, self.raw_data)


nm = NetworkManager()
p = IPAddressParser(nm.ifconfig())

print p.parse_ipv4_addresses()