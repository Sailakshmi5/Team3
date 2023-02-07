import pytest
from Level1.SystemDriveFinder  import SystemDriveFinder
from Level1.SearchFile1 import FileFinder
class Test_Drive:
    def test_DriveCase(self):
        obj=SystemDriveFinder()
        self.expected=obj.find_drives()
        self.actual=['C']
        assert self.expected==self.actual
    def test_searchfile(self):
        obj=FileFinder()
        d=obj.find_file('demo1.txt','C:\hcl')
        self.expected_filename=d[0]
        self.actual_res='C:\\hcl\\demo1.txt'
        assert self.expected_filename==self.actual_res


