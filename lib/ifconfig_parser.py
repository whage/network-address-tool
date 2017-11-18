import re
import subprocess

class IfconfigParser:
    def __init__(self, command_output = None):
        self.raw_data = command_output

        if not command_output:
        	self.raw_data = subprocess.getoutput(["ifconfig"])

    def parse_ipv4_addresses(self):
        expression = "inet addr:(\S+).*Mask:(\S+)"
        tuples = re.findall(expression, self.raw_data)

        return [(t[0], t[1]) for t in tuples]