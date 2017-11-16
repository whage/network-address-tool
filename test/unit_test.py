import unittest
 
class NetAddToolTest(unittest.TestCase):

    def test_mask_to_prefix(self):
        p = IfconfigParser()
        self.assertEqual(12, p.mask_to_prefix("255.240.0.0"))
        self.assertEqual(16, p.mask_to_prefix("255.255.0.0"))
 
    def test_parses_ifconfig_correctly(self):
        test_string = "inet addr:172.16.17.3  P-t-P:172.16.17.3  Mask:255.255.255.0" \
            "inet addr:192.168.0.10  Bcast:192.168.0.255  Mask:255.255.0.0"

        p = IfconfigParser(test_string)

        self.assertEqual([
            ("172.16.17.3", "255.255.255.0", "24"),
            ("192.168.0.10", "255.255.0.0", "16"),
        ], p.parse_ipv4_addresses())

    def test_overlapping_subnets(self):
        pass