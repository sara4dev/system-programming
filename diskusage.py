import sys
import json
from os import walk
from os.path import join, getsize
import model


class DiskUsage:
    def __init__(self, osWrapper):
        self.osWrapper = osWrapper

    def list_files(self, path):
        diskUsage = model.DiskUsage()
        for root, dirs, files in self.osWrapper.dirWalk(path):
            for name in files:
                file = model.File(
                    name=join(root, name),
                    size=self.osWrapper.getSize(join(root, name))
                )
                diskUsage.files.append(file)

        return json.dumps(diskUsage.to_json(), indent=4)


class OsWrapper:
    def dirWalk(self, path):
        return walk(path)

    def getSize(self, file):
        return getsize(file)


def main(path):
    diskUsage = DiskUsage(OsWrapper())
    print diskUsage.list_files(path)


if __name__ == "__main__":
    main(sys.argv[1])
