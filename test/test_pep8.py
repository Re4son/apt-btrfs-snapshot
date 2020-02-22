
import os
import subprocess
import unittest


class PackagePep8TestCase(unittest.TestCase):

    def test_pep8(self):
        basepath = os.path.abspath(
            os.path.join(os.path.dirname(__file__), ".."))
        res = subprocess.call(["/usr/bin/pep8", "--repeat", basepath])
        self.assertEqual(res, 0)


if __name__ == "__main__":
    unittest.main()
