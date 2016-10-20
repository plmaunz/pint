# -*- coding: utf-8 -*-
from pint import UnitRegistry, set_application_registry
from pint.testsuite import QuantityTestCase

ureg = UnitRegistry()
set_application_registry(ureg)
Q = ureg.Quantity

class TestMod(QuantityTestCase):
    def test_mod(self):
        self.assertEqual(Q(21) % 5, 1)
        self.assertEqual(Q(21) % Q(5), 1)
        self.assertEqual(21 % Q(5), 1)
        self.assertEqual(Q(21, 'inch') % Q(5, 'inch'), Q(1, 'inch'))

        x = 21
        x %= Q(5)
        self.assertEqual(x, 1)

        y = Q(21)
        y %= Q(5)
        self.assertEqual(y, 1)

        z = Q(21)
        z %= 5
        self.assertEqual(z, 1)

        w = Q(21, 'inch')
        w %= Q(5, 'inch')
        self.assertEqual(w, Q(1, 'inch'))
