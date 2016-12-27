import openpyxl
import math
import matrix
import numpy as np
import random
import uniform_distribution as ud
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import excel_transfer
import gaussian_distribution

#Gaussian random processes lab 2
class PFR:
    def __init__(self):
        self.alpha = matrix.Vector([], "Initial vectror")
        self.arnum = matrix.Vector([], "Array of random numbers")
        self.a = matrix.Matrix([[0]], "Initial matrix")
        #In this case data_array is array of random numbers
        self.data_array = matrix.Vector([], "Array of our data :)")
        self.amount_of_numbers = 1
        self.amount_of_processes = 1
        self.step = 1
        self.raw_data = {'amount': {'processes': 1, 'numbers': 1, 'realizations': 1}, 'step': 0.01}
        self.result_data = {}
        self.amount_of_intervals = 9
        self.confidence = 0.95
        self.chi_squared = None
        self.critical_value = None
        self.p_value = None
        self.result = None

        self.makedafault()

        #self.chud = ud.CheckHUD(self.alpha.vector, len(self.alpha.vector), self.confidence)

        self.commands = {
            "none": 0,
            "exit": 1,
            "test": 2,
            "clear": 3,
            "help": 4,
            "new": 5,
            "show slist": 6,
            "mk": 8,
            "start": 9,
            "transfer list": 10,
            "exp list": 11,
            "show image rl": 12,
            "start show image rl": 13,
            "show first image": 14,
            "show second image": 15,
            "show third image": 16

        }
        pass

    def importparam(self, accuracy):
        self.accuracy = accuracy

    def makedafault(self):
        self.setpath("./")
        self.setfilename("file.xlsx")
        self.setsheetname("Sheet2")
        self.acount = 1000
        #self.raw_data = {'amount': {'processes': 200, 'numbers': 100, 'realizations': 100}, 'step': 0.01}
        self.raw_data = {'amount': {'processes': 100000, 'numbers': 1000, 'realizations': 100}, 'step': 0.01, 'lambda': 10,
                         'number_of_event': 4, 'start': 1, 'end': 4, 'n': 3, 't': 3}

        self.amount_of_numbers = 1000
        self.sample_size = 10
        self.amount_of_tries = 100

        self.amount_of_intervals = 9
        self.confidence = 0.95


        # alpha in numpy format of array
        self.anp = np.random.sample(self.acount)
        # alpha in matrix format of array (vector format)
        self.alpha = matrix.Vector(self.anp.tolist(),"Random values")
        pass

    def setpath(self, path):
        self.path = path
        pass

    def setsheetname(self, sheetname):
        self.sheetname = sheetname
        pass

    def setfilename(self, filename):
        self.filename = filename
        pass

    def getfilepath(self):
        return self.path + self.filename
        pass

    def enterCommand(self):
        command = "0"
        print('')
        print("Enter command (help for Q&A)")
        while (command not in self.commands):
            command = input("->")
            if (command not in self.commands):
                print("There is no such command")
            else:
                return self.commands[command]

    def showCommands(self):
        print('')
        print("Commands...")
        for item in self.commands:
            print(str(item) + ": " + str(self.commands[item]))

    def showHelp(self):
        print('')
        print("Help v0.001")
        print("Author of this program: Sir Oleksiy Polshchak")
        self.showCommands()

    def dostaff(self):
        task = 0
        while (task != 1):
            print('')
            print("Computing by Monte Carlo`s method (task3) v0.0002 beta task #5")
            print("Modeling random values witch uniform distributed on current area...")
            print('')
            task = self.enterCommand()
            if (task == 2):
                self.dostaff()
            elif (task == 3):
                pass
            elif (task == 4):
                self.showHelp()
            elif (task == 5):
                self.inputnewdata()
                pass
            elif (task == 6):
                print(self.raw_data)
                pass
            elif (task == 8):
                self.makedafault()

            elif task == 9:
                self.resolve()
                pass
            elif task == 10:
                self.transferlist()
                pass
            elif task == 11:
                #self.show_expression_list()
                pass
            elif task == 12:
                self.build_image_realizations()
                pass
            elif task == 13:
                self.resolve()
                self.build_image_realizations()
            elif task == 14:
                self.show_first_task()
            elif task == 15:
                self.show_second_task()
            elif task == 16:
                self.show_third_task()
        pass

    def inputnewdata(self):
        task = 0
        print('')
        print("Enter count of alphas:")
        while (task != 1):
            self.accuracy = int(input("-> "))
            print("Input is correct? (enter - yes/n - no)")
            command = input("-> ")
            if (command != "n"):
                task = 1


    def inputmatrix(self):
        print('')
        i = 0
        task = 0
        return self.transferlist(param='square')

    def printresult(self):
        #print("\n")
        pass

    def show_present_data(self):
        pass

    def generate_random_numbers(self):
        #Here we will generate random numbers
        #self.data_array = self.chud.generate_random_numbers([0.0, 1.0], self.acount)
        pass

    def transferlist(self):
        self.exeldata = excel_transfer.Excel()
        self.alpha = self.exeldata.transferlist('hvectror')


    def resolve(self):
        self.result_data = PFR.analyse_process(self.raw_data, self.result_data)
        pass

    def build_image_realizations(self):
        #agr: self, raw_data, result_data
        height = [i for i in range(len(self.result_data['realizations'][0][0]))]
        plt.errorbar(self.result_data['realizations'][0][0], height, xerr=self.result_data['realizations'][0][1], ecolor='r')
        plt.errorbar(self.result_data['realizations'][1][0], height, xerr=self.result_data['realizations'][1][1], ecolor='b')
        plt.show()

    #def build_image(self):
    #    #agr: self, raw_data, result_data
    #    height = [i for i in range(len(self.data['realizations'][0][0]))]
    #    plt.errorbar(self.data['realizations'][0][0], height, xerr=self.data['realizations'][0][1], ecolor='r')
    #    plt.errorbar(self.data['realizations'][1][0], height, xerr=self.data['realizations'][1][1], ecolor='b')
    #    plt.show()

    def show_first_task(self):
        plt.hist(self.result_data['times'])
        plt.show()

    def show_second_task(self):
        plt.hist(self.result_data['intervals'])
        plt.show()

    def show_third_task(self):
        plt.hist(self.result_data['pr'])
        plt.show()

    def sync_data(self):
        pass

    #------------------

    @staticmethod
    def model_poisson_process(raw_data):
        # arg: amount_of_numbers, _lambda
        #random_numbers = np.random.uniform(size=raw_data['amount']['numbers'])
        random_numbers = np.random.uniform(size=raw_data['amount']['numbers'])
        x_n = [-math.log(random_numbers[i]) / raw_data['lambda'] for i in range(raw_data['amount']['numbers'])]
        distr = [sum(x_n[:i]) for i in range(raw_data['amount']['numbers'])]

        return distr, x_n

    @staticmethod
    def get_realizations(raw_data):
        # arg: amount_of_realizations, amount_of_numbres, _lambda
        processes = []
        for i in range(raw_data['amount']['realizations']):
            processes.append(PFR.model_poisson_process(raw_data)[0])

        return processes

    @staticmethod
    def find_time_of_first_event_appearance(result_data, raw_data):
        # arg: realizations, number_of_event
        times = [sum(result_data['realizations'][i][:raw_data['number_of_event'] + 1]) for i in range(len(result_data['realizations']))]

        return times

    @staticmethod
    def find_interval_within_events(result_data, raw_data):
        # arg: realizations, start, end
        intervals = [sum(result_data['realizations'][i][raw_data['start']: raw_data['end'] + 1]) for i in range(len(result_data['realizations']))]
        return intervals

    @staticmethod
    def find_probabilities_of_n_events_appearance(result_data, raw_data):
        # arg: realizations, n, t
        t_min = min([sum(result_data['realizations'][i]) for i in range(len(result_data['realizations']))])
        if raw_data['t'] > t_min:
            raise ValueError("T is too big")

        probabilities = []
        for k in range(100):
            size = int(len(result_data['realizations']) / 100)
            amount_of_events = []
            length = len(result_data['realizations'][0])

            for i in range(k * size, (k + 1) * size):
                time = 0
                amount = 0
                for j in range(length):
                    if time > raw_data['t']:
                        break
                    amount = j
                    time += result_data['realizations'][i][j]
                amount_of_events.append(amount)

            probabilities.append(amount_of_events.count(raw_data['n']) / size)
        return probabilities

    @staticmethod
    def analyse_process(raw_data, result_data):
        # arg: _lambda, amount_of_processes, amount_of_numbers, number_of_event, start, end, n, t
        realizations = PFR.get_realizations(raw_data)
        result_data['realizations'] = PFR.get_realizations(raw_data)

        #times = find_time_of_first_event_appearance(realizations, number_of_event)
        times = PFR.find_time_of_first_event_appearance(result_data, raw_data)

        intervals = PFR.find_interval_within_events(result_data, raw_data)
        #intervals = find_interval_within_events(realizations, start, end)

        pr = PFR.find_probabilities_of_n_events_appearance(result_data, raw_data)
        #pr = find_probabilities_of_n_events_appearance(realizations, n, t)

        #realization = (
        #model_poisson_process(amount_of_numbers, _lambda), model_poisson_process(amount_of_numbers, _lambda))

        #print(exp(-_lambda * t) * (_lambda * t) ** n / factorial(n))

        realization = (
            PFR.model_poisson_process(raw_data), PFR.model_poisson_process(raw_data))

        print(math.exp(-raw_data['lambda'] * raw_data['t']) * (raw_data['lambda'] * raw_data['t']) ** raw_data['n'] / math.factorial(raw_data['n']))

        return {
            'realizations': realization,
            'times': times,
            'intervals': intervals,
            'pr': pr
        }
