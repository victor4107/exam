import unittest as ut
import exam as ex
import sys

class MyTest(ut.TestCase): #створення класу для реалізації тестів
    def setUp(self):
        self.mp=ex.week
        
    def test_usage1(self):#створення функції для тесту
        self.assertIn(b, 31) 
        sys.stdout.flush()
    
if __name__ == "__main__":
    ut.main()#команда яка запускає всі тести із заданого модуля
