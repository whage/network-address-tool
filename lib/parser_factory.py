import os

from lib.ifconfig_parser import IfconfigParser
from lib.ip_parser import IpParser

class ParserFactory:
    def get_parser(self):
        possible_paths = ['/sbin', '/usr/sbin', '/bin', '/usr/bin']

        # try to us ip command
        for path in possible_paths:
            if os.path.exists(path + '/ip'):
                return IpParser()

        # fall back to ifconfig
        for path in possible_paths:
            if os.path.exists(path + '/ifconfig'):
                return IfconfigParser()
