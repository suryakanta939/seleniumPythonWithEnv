import unittest
from tests.practice.test_other_for_test_suite import TestOtherElement
from tests.home.test_login_for_test_suite import TestLogin

testCase1=unittest.TestLoader().loadTestsFromTestCase(TestOtherElement)
testCase2=unittest.TestLoader().loadTestsFromTestCase(TestLogin)

test_functional=unittest.TestSuite([testCase1,testCase2])

unittest.TextTestRunner().run(test_functional)