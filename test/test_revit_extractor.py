import unittest
from revit_extract.RevitExtractor import RevitExtractor


class TestRevitExtractor(unittest.TestCase):

    def setUp(self):
        self.rvt_path = r"D:\_WIP\Download\Sample Office Building Model V1.rvt"

    def test_extract_svf(self):
        output = RevitExtractor(self.rvt_path).extract_svf("output")
        print(output)

    def test_read_prob_data(self):
        output = RevitExtractor(self.rvt_path).read_prob_data()
        categories = output.get_all_categories()
        # print all dictionary
        for key in categories:
            print(key, categories[key])


if __name__ == '__main__':
    unittest.main()
