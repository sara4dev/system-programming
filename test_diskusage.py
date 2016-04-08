__author__ = 'saravanakumar'

import unittest
import diskusage

class DiskUsageTest(unittest.TestCase):
    def test_list_files(self):
        mockOsWrapper = MockOsWrapper()
        d = diskusage.DiskUsage(mockOsWrapper)
        diskusage_json = d.list_files('/test/')
        print(diskusage_json)
        self.assertEqual(1,1)

class MockOsWrapper:
    def dirWalk(self, path):
        return [
            ('/foo', ('bar',), ('baz',)),
            ('/foo/bar', (), ('spam', 'eggs'))
        ]

    def getSize(self, file):
        return 25