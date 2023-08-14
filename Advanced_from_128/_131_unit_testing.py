# test runner (unittest , pytest)

# Test case vs Test Suite vs Test Report

import unittest

"""
assert 4 * 20 == 80 , "Should be 80"

def test_multiply_5_20():
    assert 5 * 20 == 100 , "Should be 100"

def test_multiply_50_5():
    assert 5 * 50 == 250 , "Should be 250"


if __name__ == '__main__':
   test_multiply_5_20()
   test_multiply_50_5()
   print("All Tests Passed")
*/
"""

class test_post_controller(unittest.TestCase):
    def test_show_posts(self):
        self.assertCountEqual(["Mohamed","ahmed"],("Mohamed","ahmed"),"Should First Count Equal To Second Count")

    def test_equal(self):
        self.assertEqual(20 * 100,2000,"Should be 2000")

    def test_using_true(self):
        self.assertTrue(100 == 50 + 50 , "Should Be True")

if __name__ == '__main__':
    unittest.main()
