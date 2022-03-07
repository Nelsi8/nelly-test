import unittest
from unittest.mock import Mock
import csvparser

class TestParser(unittest.TestCase):
    def test_read_row(self):
        file = Mock()
        file.configure_mock(
            **{'readline.return_value':'\'Vehicle1\',\'Vehicle2\''})
#expect

expected = ("'Vehicle1' - 'Vehicle2'")
        
#result
result = csvparser.read_row(file)
print(result)

#assert
assert result == expected
if __name__ == "__main__":
    unittest.main()

