from numpy.random import uniform
from math import sin, cos, sqrt
# program use sin(), cos(), and sqrt(), when expression contain this functions

class MCintegral:
    def monte_сarlo_method(self, expression, a, b, amount_of_intervals):
        #'a' and 'b' are borders of integral
        random_numbers = uniform(a, b, amount_of_intervals)
        # s - is sum of literals (result of expression)
        # program call function witch in this case expression, so program run expression and
        # return result
        s = sum(self.execute_expression(expression, random_numbers[i]) for i in range(len(random_numbers)))
        integral = (float(b - a) / amount_of_intervals) * s
        return integral

    def execute_expression(self, function, x):
        return eval(function)

    def count(self, expression, boundary, amount_of_intervals):
        result = self.monte_сarlo_method(expression, boundary[0], boundary[1], amount_of_intervals)
        return result