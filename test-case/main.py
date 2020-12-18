import unittest
from selenium import webdriver
import page


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("https://www.python.org/")

    def test_example(self) -> None:
         print("True")
        assert True

    def tearDown(self):
        self.driver.close)()

if __name__ = "__main__"
        unittest.main()