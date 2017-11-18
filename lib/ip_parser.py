import re

from lib.base_parser import BaseParser

class IpParser(BaseParser):
    def __init__(self, command_output = None):
        self.command = "ip a"
        self.init_raw_data(command_output)

    def parse_ipv4_addresses(self):
        expression = "inet (\S+).*?\/(\d*)"
        matches = re.findall(expression, self.raw_data)

        return [(m[0], m[1]) for m in matches]