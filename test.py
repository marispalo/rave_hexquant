#!/usr/bin/env python
'''
Copyright (C) 2015- Swedish Meteorological and Hydrological Institute (SMHI)

This file is part of RAVE, sort-of ...

RAVE is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

RAVE is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with RAVE.  If not, see <http://www.gnu.org/licenses/>.
'''

## Simple example unit testing framework

## @file
## @author Daniel Michelson, SMHI
## @date 2015-06-03

import unittest
import rave_hexquant

class TestHex(unittest.TestCase):
    """
    Our basic test class
    """

    def test_q2hex(self):
        """
        Test q2hex
        Any method which starts with ``test_`` will considered as a test case.
        """
        result = rave_hexquant.q2hex(["TH","DBZH"])
        self.assertEqual(result, '0x3')
        
    def test_hex2q(self):
        """
        Test hex2q
        Any method which starts with ``test_`` will considered as a test case.
        """
        result = rave_hexquant.hex2q('0x3')
        self.assertEqual(result, ["TH","DBZH"])
        
    def test_hex2long(self):
        result=rave_hexquant.hex2long(rave_hexquant.q2hex(["TH","DBZH"]))
        print result
        self.assertEqual(result, 3)
        





if __name__ == '__main__':
    unittest.main()
