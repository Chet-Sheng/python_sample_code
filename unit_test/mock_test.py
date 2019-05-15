import unittest
from unittest import TestCase, mock

from work import work_on


class TestWorkMockingModule(TestCase):

    def test_using_context_manager(self):
        with mock.patch('work.os') as mocked_os:
            work_on()  # when this runs, it calls mocked_os.getcwd() once
            mocked_os.getcwd.assert_called_once()


if __name__ == '__main__':
    unittest.main()