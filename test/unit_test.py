import unittest

from lib.ifconfig_parser import IfconfigParser
from lib.subnet_manager import SubnetManager
from lib import util

class NetAddToolTest(unittest.TestCase):
    def test_mask_to_prefix(self):
        self.assertEqual(12, util.mask_to_prefix("255.240.0.0"))
        self.assertEqual(16, util.mask_to_prefix("255.255.0.0"))
 
    def test_parses_ifconfig_correctly(self):
        with open('test/data/ifconfig_sample.txt') as f:
            test_string = f.read()

        p = IfconfigParser(test_string)

        self.assertEqual([
            ("192.168.1.29", "255.255.255.0"),
            ("127.0.0.1", "255.0.0.0"),
            ("192.168.1.64", "255.240.0.0"),
            ("172.16.17.3", "255.255.192.0"),
            ("4.5.0.3", "255.255.0.0"),
            ("4.5.2.1", "255.255.252.0"),
        ], p.parse_ipv4_addresses())

    def test_overlapping_subnets(self):
        pass