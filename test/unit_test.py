import unittest

from netaddrtool.lib.ifconfig_parser import IfconfigParser
from netaddrtool.lib.subnet_manager import SubnetManager
from netaddrtool.lib import util
 
class NetAddToolTest(unittest.TestCase):
    def test_mask_to_prefix(self):
        self.assertEqual(12, util.mask_to_prefix("255.240.0.0"))
        self.assertEqual(16, util.mask_to_prefix("255.255.0.0"))
 
    def test_parses_ifconfig_correctly(self):
        with open('test/data/ifconfig_sample.txt') as f:
            test_string = f.read()

        p = IfconfigParser(test_string)

        self.assertEqual([
            ("192.168.1.29", "255.255.255.0", 24),
            ("127.0.0.1", "255.0.0.0", 8),
            ("192.168.1.64", "255.240.0.0", 12),
            ("172.16.17.3", "255.255.192.0", 18),
        ], p.parse_ipv4_addresses())

    def test_overlapping_subnets(self):
        pass