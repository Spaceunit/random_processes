from math import pi, log, sin, cos, sqrt, exp

from numpy import histogram
from numpy.random import random
from scipy.stats import chi2
import matplotlib.pyplot as plt

class Gaussiandistribution:
    @staticmethod
    def model_gaussian_distribution(amount_of_numbers, amount_of_intervals, confidence):
        hi = []
        # xi U+03C7 U+03B1 {χi} = {sqrt(-2 * log[10](α[1])) * cos(2 * pi * α[2])}[times amount_of_numbers]
        hi.append([sqrt(-2 * log(random())) * cos(2 * pi * random()) for _ in range(amount_of_numbers)])

        # xi U+03C7 U+03B1 {χi} = {sqrt(-2 * log[10](α[1])) * sin(2 * pi * α[2])}[times amount_of_numbers]
        hi.append([sqrt(-2 * log(random())) * sin(2 * pi * random()) for _ in range(amount_of_numbers)])

        # xi U+03C7 U+03B1 {χi} = {Σ[times 3](-2 * (α[1] - 0.5))}[times amount_of_numbers]
        hi.append([sum(2 * (random() - 0.5) for _ in range(3)) for i in range(amount_of_numbers)])

        # xi U+03C7 U+03B1 {χi} = {Σ[times 12](α[1] - 0.5))}[times amount_of_numbers]
        hi.append([sum(random() - 0.5 for _ in range(12)) for i in range(amount_of_numbers)])

        # xi U+03C7 U+03B1 {χi} = {Σ[times 48](0.5 * (α[1] - 0.5))}[times amount_of_numbers]
        hi.append([sum(0.5 * (random() - 0.5) for _ in range(48)) for i in range(amount_of_numbers)])

        #plt.hist(hi[0], amount_of_intervals)
        #plt.show()

        for i in range(len(hi)):
            plt.figure(i + 1)
            plt.hist(hi[i], amount_of_intervals)

        plt.show()

        #distr1 = Gaussiandistribution.check_hypothesis_about_normal_distribution(xi1, 9, 0.95)

        distr = [Gaussiandistribution.check_hypothesis_about_normal_distribution(hi[i], amount_of_intervals, confidence) for i in range(len(hi))]

        return {
            'distr1': distr[0],
            'distr2': distr[1],
            'distr3': distr[2],
            'distr4': distr[3],
            'distr5': distr[4]
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
