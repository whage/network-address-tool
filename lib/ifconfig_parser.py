import re

class IfconfigParser:
    def __init__(self, ifconfig_output):
        self.raw_data = ifconfig_output

    def parse_ipv4_addresses(self):
        expression = "inet addr:(\S+).*Mask:(\S+)"
        tuples = re.findall(expression, self.raw_data)

        return [(t[0], t[1]) for t in tuples]