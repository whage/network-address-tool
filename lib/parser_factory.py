import os

from lib import IfconfigParser
from lib import IpParser

class ParserFactory:
    def get_parser(self):
        possible_paths = ['/sbin', '/usr/sbin', '/bin', '/usr/bin']

        for path in possible_paths:
            if os.path.exists(path + '/ifconfig')):
                return IfconfigParser()

        for path in possible_paths:
            if os.path.exists(path + '/ip')):
                return IpParser()
