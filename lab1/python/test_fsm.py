import unittest, os
from fsm import fsm

def parseTests(filename):
    tests = []
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    for line in lines:
        test = []
        line = line.rstrip()
        for test_case in line.split(' '):
            data = test_case.split('/')
            int_data = map(int, data)
            test.append(tuple(int_data))
        tests.append(test)
    
    return tests

class TestFSM(unittest.TestCase):
    tests = []
    @classmethod
    def setUpClass(self):
        self.tests = parseTests('/Users/artemandruhov/src/formal/lab1/tests')
        
    def test_fsm_correct(self):
        f = fsm.FSM()
        inputs = [0,1, 0,1,1,1, 0,1,1,0]
        outputs = [0,1, 0,1,1,0, 0,1,1,0]
        for case in list(zip(inputs,outputs)):
            self.assertEqual(f.process(case[0]), bool(case[1]))
    
    def test_fsm_mutants(self):
        f = fsm.FSM()
        for test in self.tests:
            print('Running test', test)
            f.reset()
            for case in test:
                self.assertEqual(f.process(case[0]), bool(case[1]))
            
if __name__ == '__main__':
    # tests = parseTests('../tests')
    unittest.main()