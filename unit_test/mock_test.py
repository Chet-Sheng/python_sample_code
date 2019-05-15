import unittest
from unittest import TestCase, mock

from work import work_on
from worker import Worker, Helper


class TestWorkMockingModule(TestCase):

    def test_using_context_manager(self):
        with mock.patch('work.os', autospec=True) as mocked_os:
            work_on()  # when this runs, it calls mocked_os.getcwd() once
            # it substitute os with mocked_os, ie. a mock instance
            mocked_os.getcwd.assert_called_once()

    @mock.patch('work.os')  # so work.os would be mocked
    def test_using_decorator(self, mocked_os):
        work_on()
        mocked_os.getcwd.assert_called_once()


class TestWorkerModule(TestCase):

    def test_patching_class(self):
        with mock.patch('worker.Helper', autospec=True) as MockHelper:  # mocking class here not the instance
            # MockHelper().get_path.return_value = 'testing'
            MockHelper.return_value.get_path.return_value = 'testing'
            # MockHelper.get_path.return_value would not work:
            # since in the code we call get_path on an instance, not the class itself.
            worker = Worker()
            MockHelper.assert_called_once_with('db')
            # print(MockHelper.shit())  # this will pass if there's no autospec=True, as .shit() is a new attribute of mocker instance
            self.assertEqual(worker.work(), 'testing')


class TestWorker(TestCase):
    def test_partial_patching(self):
        with mock.patch.object(Helper, 'get_path', return_value='testing'):
            worker = Worker()
            self.assertEqual(worker.helper.path, 'db')
            self.assertEqual(worker.work(), 'testing')


if __name__ == '__main__':
    unittest.main()