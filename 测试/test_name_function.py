import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够处理"""

        full_name = get_formatted_name(first='joy', last='worden')
        self.assertEqual(full_name, 'Joy Worden')

    def test_first_null_name(self):
        """测试first=''的情况"""

        full_name = get_formatted_name('', last='worden')
        self.assertEqual(full_name, ' Worden')


unittest.main()
