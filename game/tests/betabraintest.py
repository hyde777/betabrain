import unittest
import betabrain

class TestBetaBrainGame(unittest.TestCase):
    def setUp(self):
        betabrain.tries = list()

    def test_generate_solution(self):
        solution = betabrain.generateProblem()
        self.assertEqual(len(solution), 5)

    def test_problem_content(self):
        solution = betabrain.generateProblem()
        for p in solution:
            self.assertEqual(p in betabrain.colors, True)

    def test_correct_checker_output(self):
        problem = ['R', 'B', 'W', 'R', 'G']

        solution = problem

        self.assertEqual(betabrain.check(problem, solution), (5, 0))

    def test_missplaced_pegs_checker_output(self):
        problem = ['R', 'B', 'W', 'R', 'G']

        solution = ['G', 'G', 'G', 'W', 'W']

        self.assertEqual(betabrain.check(problem, solution), (0, 2))

    def test_full_false_pegs(self):
        problem = ['R', 'R', 'R', 'R', 'R']
        solution = ['G', 'G', 'G', 'G', 'G']

        self.assertEqual(betabrain.check(problem, solution), (0, 0))

    def test_incorrect_checker_output(self):
        problem = ['R', 'B', 'W', 'R', 'G']
        solution = ['R', 'R', 'G', 'R', 'W']

        self.assertEqual(betabrain.check(problem, solution), (2, 2))

    def test_tries(self):
        solution = ['R', 'P', 'G', 'R', 'G']
        problems = (['R', 'B', 'W', 'R', 'G'], ['R', 'R', 'P', 'R', 'G'])

        for problem in problems:
            betabrain.check(problem, solution)

        result = list([(['R', 'B', 'W', 'R', 'G'], (3, 0)), (['R', 'R', 'P', 'R', 'G'], (3, 2))])

        self.assertEqual(len(betabrain.tries), 2)
        self.assertEqual(betabrain.tries, result)

if __name__ == '__main__':
    unittest.main()
