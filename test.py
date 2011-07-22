#! /usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import statestyle


class BaseTest(unittest.TestCase):
    
    def setUp(self):
        self.good_postals = ['CA', 'IA', 'dc', 'iL',]
        self.bad_postals = ['XX', 'xx', 'Xx',]
        self.good_names = ['California', 'Iowa', 'district of columbia', 'ILLINOIS']
        self.bad_names = ['Los Angeles', 'Cedar Rapids', 'Shaw', 'CHICAGO']
        self.good_fips = ['06', '19', 11, 17]
        self.bad_fips = [-6, '190', '11 ', 0]
        self.good_ap = ['Calif.', 'Iowa', 'd.c.', 'ILL.']
        self.bad_ap = ['Cali', 'iow', 'CD', 'ILLI']

class GetTest(BaseTest):
    
    def test_attr(self):
        obj = statestyle.get("CA")
        self.assertEqual(obj.postal, 'CA')
        self.assertEqual(obj.fips, '6')
        self.assertEqual(obj.name, 'California')
        self.assertEqual(obj.type, 'state')
        self.assertEqual(obj.ap, 'Calif.')
    
    def test_postals(self):
        [statestyle.get(i) for i in self.good_postals]
        [self.assertRaises(ValueError, statestyle.get, i) for i in self.bad_postals]

    def test_names(self):
        [statestyle.get(i) for i in self.good_names]
        [self.assertRaises(ValueError, statestyle.get, i) for i in self.bad_names]

#    def test_fips(self):
#        [statestyle.get(i) for i in self.good_fips]
#        [self.assertRaises(ValueError, statestyle.get, i) for i in self.bad_fips]

    def test_ap(self):
        [statestyle.get(i) for i in self.good_ap]
        [self.assertRaises(ValueError, statestyle.get, i) for i in self.bad_ap]


if __name__ == '__main__':
    unittest.main()
