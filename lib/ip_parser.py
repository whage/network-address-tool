import re
import subprocess

class IpParser:
    def __init__(self, command_output = None):
        self.raw_data = command_output

        if not command_output:
        	self.raw_data = subprocess.getoutput(["ip a"])

    def parse_ipv4_addresses(self):
        expression = "inet (\S+).*?\/(\d*)"
        matches = re.findall(expression, self.raw_data)

        return [(m[0], m[1]) for m in matches]