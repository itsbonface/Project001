import pytest

#Single test
def function(x):
    return x + 3

def test_function():
    assert function(7) == 10

#Move to file directory and run "$ pytest filename.py"


#Multiple tests
class TestSomeFunctions():
    def test_func1(self):
        x = 'greentage0010'
        assert 'g' in x
    
    def test_func2(self):
        y = [3, 7, 6]
        assert hasattr(y, 3)

