__author__ = 'saravanakumar'

import unittest
import diskusage
import json

class DiskUsageTest(unittest.TestCase):
    def test_list_files(self):
        mockOsWrapper = MockOsWrapper()
        d = diskusage.DiskUsage(mockOsWrapper)
        diskusage_dict = json.loads(d.list_files('/test/'))
        self.assertEqual(25, diskusage_dict['files'][0]['size'])
        self.assertEqual(3, len(diskusage_dict['files']))

class MockOsWrapper:
    def dirWalk(self, path):
        return [
            ('/foo', ('bar',), ('baz',)),
            ('/foo/bar', (), ('spam', 'eggs'))
        ]

    def getSize(self, file):
        return 25