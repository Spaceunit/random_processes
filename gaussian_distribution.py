from math import pi, log, sin, cos, sqrt, exp

from numpy import histogram
from numpy.random import random
from scipy.stats import chi2

class Gaussiandistribution:
    @staticmethod
    def model_gaussian_distribution(amount_of_numbers):
        # xi U+03C7 U+03B1 {χi} = {sqrt(-2 * log[10](α[1])) * cos(2 * pi * α[2])}
        xi1 = [sqrt(-2 * log(random())) * cos(2 * pi * random()) for _ in range(amount_of_numbers)]

        # xi U+03C7 U+03B1 {χi} = {sqrt(-2 * log[10](α[1])) * sin(2 * pi * α[2])}
        xi2 = [sqrt(-2 * log(random())) * sin(2 * pi * random()) for _ in range(amount_of_numbers)]

        # xi U+03C7 U+03B1 {χi} = Σ(2 * ())
        xi3 = [sum(2 * (random() - 0.5) for _ in range(3)) for i in range(amount_of_numbers)]

        xi4 = [sum(random() - 0.5 for _ in range(12)) for i in range(amount_of_numbers)]
        xi5 = [sum(0.5 * (random() - 0.5) for _ in range(48)) for i in range(amount_of_numbers)]

        # pyplot.hist(xi1, 9)
        # pyplot.show()

        distr1 = Gaussiandistribution.check_hypothesis_about_normal_distribution(xi1, 9, 0.95)
        distr2 = Gaussiandistribution.check_hypothesis_about_normal_distribution(xi2, 9, 0.95)
        distr3 = Gaussiandistribution.check_hypothesis_about_normal_distribution(xi3, 9, 0.95)
        distr4 = Gaussiandistribution.check_hypothesis_about_normal_distribution(xi4, 9, 0.95)
        distr5 = Gaussiandistribution.check_hypothesis_about_normal_distribution(xi5, 9, 0.95)
        return {
            'distr1': distr1,
            'distr2': distr2,
            'distr3': distr3,
            'distr4': distr4,
            'distr5': distr5
        }

    @staticmethod
    def check_hypothesis_about_normal_distribution(random_numbers, amount_of_intervals, confidence):

        observed, intervals = histogram(random_numbers, amount_of_intervals, normed=True)
        expected = [Gaussiandistribution.function((intervals[i] + intervals[i + 1]) / 2) for i in range(len(intervals) - 1)]
        chi_squared = sum(((observed[i] - expected[i]) ** 2) / expected[i] for i in range(len(observed)))

        critical = chi2.ppf(confidence, amount_of_intervals)
        p_value = chi2.sf(chi_squared, amount_of_intervals)

        return {
            'chi_squared': chi_squared,
            'critical': critical,
            'p_value': p_value

        }

    @staticmethod
    def function(x):
        return 1 / sqrt(2 * pi) * exp(-(x ** 2) / 2)

# model_gaussian_distribution(100)
