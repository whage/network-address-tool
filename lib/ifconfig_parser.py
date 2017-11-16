import re

class IfconfigParser:
    def __init__(self, str):
        self.raw_data = str

    def parse_ipv4_addresses(self):
        expression = "inet addr:(\S+).*Mask:(\S+)"
        tuples = re.findall(expression, self.raw_data)

        return [(t[0], t[1], self.mask_to_prefix(t[1])) for t in tuples]

    def mask_to_prefix(self, mask):
        return sum([bin(int(x)).count('1') for x in mask.split('.')])