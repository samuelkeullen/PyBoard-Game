from Test import TestCase

class TestClass(TestCase):

    def test1(self):
        self.main()
        
    if __name__ == "__main__":
        TestCase.main()