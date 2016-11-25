import numpy as np
from numpy import histogram
from scipy.stats import chi2

class CheckHUD:
    def __init__(self, random_numbers, count_intervals, confidence):
        self.prepare_main_parameters(random_numbers, count_intervals, confidence)

    def checkHUD(self, random_numbers, count_intervals, confidence):
        # it will used when we want use CheckHUD like static
        # intervals is n, observed is bins (look into numpy.histogram)
        intervals, observed = histogram(random_numbers, count_intervals, normed=True)
        # array n = observed of 1 :)
        expected = [1] * len(observed)

        #our Chi-squared which we will test
        chi_sq = sum(((observed[i] - expected[i]) ** 2) / expected[i] for i in range(len(observed)))
        #our Critical
        critical = chi2.ppf(1 - confidence, count_intervals - 1)
        # our P - value
        p_value = chi2.sf(chi_sq, count_intervals - 1)
        return {
            'intervals': intervals,
            'observed': observed,
            'expected': expected,
            'chi_sq': chi_sq,
            'critical': critical,
            'p_value': p_value
        }

    def prepare_main_parameters(self, random_numbers, count_intervals, confidence):
        main_param = self.checkHUD(random_numbers=random_numbers, count_intervals=count_intervals, confidence=confidence)
        self.intervals = main_param['intervals']
        self.observed = main_param['observed']
        self.expected = main_param['expected']
        self.chi_sq = main_param['chi_sq']
        self.critical = main_param['critical']
        self.p_value = main_param['p_value']

    def checkstate(self):
        print(True)

    def generate_random_numbers(self, interval, size):
        array_of_random_numbers = None
        if interval[0] < interval[1]:
            array_of_random_numbers = np.random.uniform(interval[0], interval[1], size=size)
        else:
            print("Wrong input!!!")
            array_of_random_numbers = None
        return array_of_random_numbers

