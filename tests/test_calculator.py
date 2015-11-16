# -*- coding: utf-8 -*-

import unittest
from calculator import calc
from decimal import Decimal

class CalculatorTestCase(unittest.TestCase):
    def testAdd(self):
        self.assertEquals(calc('101+202'), Decimal('303'))

    def testSub(self):
        self.assertEquals(calc('401-1'), Decimal('400'))

    def testMult(self):
        self.assertEquals(calc('2*1.5'), Decimal('3'))

    def testDiv(self):
        self.assertEquals(calc('3/1.5'), Decimal('2'))
        
    def testAdd2(self):
        self.assertEquals(calc('0.1+0.2'), Decimal('0.3'))

    def testSub2(self):
        self.assertEquals(calc('0.3-0.1'), Decimal('0.2'))

    def testMult2(self):
        self.assertEquals(calc('12*0.1'), Decimal('1.2'))

    def testDiv2(self):
        self.assertEquals(calc('0.3/0.1'), Decimal('3'))

    def testAbs(self):
        self.assertEquals(calc('|10|'), Decimal('10'))
        self.assertEquals(calc('|-1.1|'), Decimal('1.1'))

    def testLeftZero(self):
        self.assertEquals(calc('0100 + 04'), Decimal('104'))
        self.assertEquals(calc('|-01.1|'), Decimal('1.1'))

    def testFloatForms(self):
        self.assertEquals(calc('1.+.2'), Decimal('1.2'))

    def testNotString(self):
        self.assertRaises(TypeError, calc, 4)

    def testEmptyString(self):
        self.assertRaises(ValueError, calc, '')

    def testDivZero(self):
        self.assertRaises(ZeroDivisionError, calc, '1/0')

    def testSpaces(self):
        self.assertEquals(calc('   20   *  -  1.5   '), Decimal('-30'))
        self.assertRaises(ValueError, calc, '2  0 *-1.5')
        self.assertEquals(calc('  |  -  10  |  '), Decimal('10'))
        self.assertRaises(ValueError, calc, '|-1  0|')

    def testSigned(self):
        self.assertEquals(calc('-4-+2'), Decimal('-6'))
        self.assertEquals(calc('|+6|'), Decimal('6'))

    def testTooFewOperands(self):
        self.assertRaises(ValueError, calc, '/')
        self.assertRaises(ValueError, calc, '-1/')
        self.assertRaises(ValueError, calc, '/-1')
        self.assertRaises(ValueError, calc, '||')

    def testNoOperators(self):
        self.assertRaises(ValueError, calc, '12')

    def testTooManyOperators(self):
        self.assertRaises(ValueError, calc, '1*2-')
        self.assertRaises(ValueError, calc, '/1*2')
        self.assertRaises(ValueError, calc, '1//2')
        self.assertRaises(ValueError, calc, '||1|')
        self.assertRaises(ValueError, calc, '|1||')

    def testInvalidOperand(self):
        self.assertRaises(ValueError, calc, '0*one')
        self.assertRaises(ValueError, calc, '4hundred/0')
        self.assertRaises(ValueError, calc, '1+.')
        self.assertRaises(ValueError, calc, '.+2')

    def testInvalidOperator(self):
        self.assertRaises(ValueError, calc, '1|2')
        self.assertRaises(ValueError, calc, '1m2')
        self.assertRaises(ValueError, calc, '1p2')
