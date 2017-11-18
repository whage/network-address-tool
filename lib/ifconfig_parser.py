import re

from lib import util
from lib.base_parser import BaseParser

class IfconfigParser(BaseParser):
    def __init__(self, command_output = None):
        self.command = "ifconfig"
        self.init_raw_data(command_output)

    def parse_ipv4_addresses(self):
        expression = "inet addr:(\S+).*Mask:(\S+)"
        matches = re.findall(expression, self.raw_data)

        return [(m[0], util.mask_to_prefix(m[1])) for m in matches]