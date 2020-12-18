import unittest as ut
import sys
#a = int(input('введіть місяць семестру: '))
#b = int(input('введіть день місяця: '))
a=1
b=15
def week():
    if (a == 1):
        c = b/7
        d = c%2
        if d == 0:
            print('тиждень парний))')
        else:
            print('тиждень не парний))')
    if (a == 2):
        c = 31//b
        d = (c + (30//7))%2
        if d == 0:
            print('тиждень парний)))')
        else:
            print('тиждень не парний))')

week()


class MyTest(ut.TestCase): #створення класу для реалізації тестів
    
        
    def test_usage1(self):#створення функції для тесту
        self.assertIn(int(b), range(0,31)) 
        sys.stdout.flush()
        
if __name__ == "__main__":
    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    ut.main(testRunner=runner)
    ut.main()
