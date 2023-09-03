"""
This files defines tests for the exercises.
There are no exercises for you in here and you should not change the contents of this file.
You may read the test cases to get a better idea of what is expected of the functions you are asked to create during the exercises.
Note that while you could hard-code your functions to pass these tests, your code will later be tested on hidden test cases.
"""

import os
import sys
import numpy as np

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'utility', 'edutest'))
import edutest
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'scenario'))
from forage_bot import ForageBot, Tree

class Test_MeanTreeYield_Types(edutest.TestCase):
    def test(self):
        tree_one = ForageBot.pre_survey['tree_one']
        self.output_type(tree_one, [float, np.float64])

class Test_MeanTreeYield_Values(edutest.TestCase):
    def test(self):
        tree_one = ForageBot.pre_survey['tree_one']
        np.random.seed(42)
        self.io_pair(tree_one, 3.0119482650138947, approximate=True)

        tree_two = ForageBot.pre_survey['tree_two']
        np.random.seed(42)
        self.io_pair(tree_two, 5.011948265013895, approximate=True)

        # @StartHiddenCases
        tree_three = Tree(63, 12)
        np.random.seed(42)
        self.io_pair(tree_three, 63.14337918016672, approximate=True)

        tree_four = Tree(213, 437)
        np.random.seed(42)
        self.io_pair(tree_four, 279.10528472049117, approximate=True)
        # @EndHiddenCases

class Test_MeanTreeYield(edutest.TestSuite):
    test_cases = [
        Test_MeanTreeYield_Types,
        Test_MeanTreeYield_Values,
    ]

class Test_ExerciseTwo_Values(edutest.TestCase):
    def test(self):
        self.AssertEqualsApproximate(self.kwargs['ANSWER_PROB_TREE_THREE'], 0.848948636950162)
        # @StartHiddenCases
        self.AssertEqualsApproximate(self.kwargs['ANSWER_PROB_TREE_FOUR'], 0.9812197276162046)
        # @EndHiddenCases

class Test_ExerciseTwo(edutest.TestSuite):
    test_cases = [
        Test_ExerciseTwo_Values
    ]

class Test_ExerciseThree_Values(edutest.TestCase):
    def test(self):
        np.random.seed(42)
        bot = ForageBot()
        tree = self.kwargs['BRONZE_MEDAL_TREE']
        passes = 0
        for i in range(1000):
            if bot.forage(tree) > 8:
                passes += 1
        self.AssertLargerThan(passes, 749)

class Test_ExerciseThree(edutest.TestSuite):
    test_cases = [
        Test_ExerciseThree_Values
    ]