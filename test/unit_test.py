import unittest

from lib.ifconfig_parser import IfconfigParser
from lib.subnet_manager import SubnetManager
from lib import util

class NetworkAddressToolTest(unittest.TestCase):
    def test_mask_to_prefix(self):
        self.assertEqual(12, util.mask_to_prefix("255.240.0.0"))
        self.assertEqual(16, util.mask_to_prefix("255.255.0.0"))
 
    def test_parses_ifconfig_correctly(self):
        with open('test/data/ifconfig_sample.txt') as f:
            test_string = f.read()

        p = IfconfigParser(test_string)

        self.assertEqual([
            ("192.168.1.29", 24),
            ("127.0.0.1", 8),
            ("192.168.1.64", 12),
            ("172.16.17.3", 18),
            ("4.5.0.3", 16),
            ("4.5.2.1", 22),
        ], p.parse_ipv4_addresses())

    def test_overlapping_subnets(self):
        with open('test/data/ifconfig_sample.txt') as f:
            test_string = f.read()

        p = IfconfigParser(test_string)
        addresses = p.parse_ipv4_addresses()

        sm = SubnetManager()
        overlapping_pairs = sm.get_overlapping_subnets(addresses)

        self.assertEqual([
            {'192.168.1.29/24', '192.168.1.64/12'},
            {'4.5.2.1/22', '4.5.0.3/16'},
        ], overlapping_pairs)