import re
import subprocess

from . import util

class IfconfigParser:
    def __init__(self, command_output = None):
        self.raw_data = command_output

        if not command_output:
        	self.raw_data = subprocess.getoutput(["ifconfig"])

    def parse_ipv4_addresses(self):
        expression = "inet addr:(\S+).*Mask:(\S+)"
        matches = re.findall(expression, self.raw_data)

        return [(m[0], util.mask_to_prefix(m[1])) for m in matches]