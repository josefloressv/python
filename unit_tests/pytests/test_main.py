import pytest

class TestMain():
    @classmethod
    def setup_class(cls):
        print("is executed once before all tests in the class")
    
    @classmethod
    def teardown_class(cls):
        print("is executed once after all tests in the class")
    
    def setup_method(self):
        print("is executed before each test method")
    def teardown_method(self):
        print("is executed after each test method")

    def test_example(self):
        assert 1 == 1, "The test failed"

    @pytest.mark.skip(reason="I don't want to run this test")
    def test_example2(self):
        assert 1 == 1, "The test failed"

    @pytest.mark.xyz
    def test_example3(self):
        assert 1 == 1, "The test failed"
    
    @pytest.fixture
    def fixture(self):
        return 1
    def test_example4(self, fixture):
        assert fixture == 1, "The test failed"

    
    @pytest.mark.parametrize("input, expected", [(1, 2), (3, 4), (5, 6)])
    def test_example5(self, input, expected):
        assert input + 1 == expected, "The test failed"