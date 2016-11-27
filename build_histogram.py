from numpy.random import choice

class BH:
    @staticmethod
    def get_data_for_histogram(random_values, sample_size, amount_of_tries):

        result = []
        for _ in range(amount_of_tries):
            sample = choice(random_values, sample_size)
            result.append(max(sample))

        return result