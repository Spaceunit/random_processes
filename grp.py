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
class GRP:
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
            "show image": 12,
            "start show image": 13

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
        self.raw_data = {'amount': {'processes': 2000, 'numbers': 100, 'realizations': 100}, 'step': 0.01}

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
                self.alpha.showvector()
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
                self.build_image(self.raw_data, self.result_data)
                pass
            elif task == 13:
                self.resolve()
                self.build_image(self.raw_data, self.result_data)
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
        self.data_array = self.chud.generate_random_numbers([0.0, 1.0], self.acount)
        pass

    def transferlist(self):
        self.exeldata = excel_transfer.Excel()
        self.alpha = self.exeldata.transferlist('hvectror')


    def resolve(self):
        #self.generate_random_numbers()
        #self.show_present_data()
        #self.result = gaussian_distribution.Gaussiandistribution.model_gaussian_distribution(self.amount_of_numbers, self.amount_of_intervals, self.confidence)
        #self.printresult()
        #
        #self.raw_data = {'amount': {'processes': 1, 'numbers': 1, 'realizations': 1}, 'step': 0.01}
        #self.result_data = {}

        #x = list(range(amount_of_processes))
        self.raw_data['x'] = list(range(self.raw_data['amount']['processes']))
        #self.raw_data['x'] = []
        #h = 0
        #for _ in range(self.raw_data['amount']['processes']):
        #    h += self.raw_data['step']
        #    self.raw_data['x'].append(h)

        self.result_data['result'] = GRP.analyse_processes(self.raw_data)

    def build_image(self, raw_data, result_data):
        print("build_image: in process")
        realization1_0, = plt.plot(raw_data['x'], result_data['result']['first_processes_realizations'][0])
        print(realization1_0)
        realization1_1, = plt.plot(raw_data['x'], result_data['result']['first_processes_realizations'][1])
        realization2_0, = plt.plot(raw_data['x'], result_data['result']['second_processes_realizations'][0])
        realization2_1, = plt.plot(raw_data['x'], result_data['result']['second_processes_realizations'][1])
        plt.legend([realization1_0, realization1_1, realization2_0, realization2_1],
                      ['realization1_0', 'realization1_1', 'realization2_0', 'realization2_1'], loc=3)

        plt.figure()
        mean1, = plt.plot(raw_data['x'], result_data['result']['first_process'][0])
        variance1, = plt.plot(raw_data['x'], result_data['result']['first_process'][1])
        mean2, = plt.plot(raw_data['x'], result_data['result']['second_process'][0])
        variance2, = plt.plot(raw_data['x'], result_data['result']['second_process'][1])
        plt.legend([mean1, variance1, mean2, variance2], ['mean1', 'variance1', 'mean2', 'variance2'])
        print("build_image: builded")
        plt.show()

    def sync_data(self):
        pass

    @staticmethod
    def model_first_process(t, amount_of_numbers, r1, r2):
        xi = []
        for i in range(amount_of_numbers):
            eta = 1 / (1 + math.pi * i ** 2)
            #eta = 1
            arg = i * math.pi * t
            xi.append((math.cos(arg) * r1[i] + math.sin(arg) * r2[i]) * eta)
            #xi.append(math.cos(arg) * r1[i] + math.sin(arg) * r2[i])
        return sum(xi)

    @staticmethod
    def model_second_process(t, amount_of_numbers, r1, r2, r3):
        xi = []
        for i in range(amount_of_numbers):
            eta = 1 / math.sqrt(1 + math.pi * i ** 2) ** 2
            arg = r3[i] * t
            xi.append((math.cos(arg) * r1[i] + math.sin(arg) * r2[i]) * eta)
            #xi.append(math.cos(arg) * r1[i] + math.sin(arg) * r2[i])

        return sum(xi)

    @staticmethod
    def analyse_processes(raw_data):
        print("analyse_processes: in process")
        processes1 = []
        processes2 = []
        for _ in range(raw_data['amount']['realizations']):
            r1 = [math.sqrt(-2 * math.log(random.random())) * math.cos(2 * math.pi * random.random()) for _ in
                  range(raw_data['amount']['numbers'])]
            r2 = [math.sqrt(-2 * math.log(random.random())) * math.sin(2 * math.pi * random.random()) for _ in
                  range(raw_data['amount']['numbers'])]
            r3 = [random.uniform(i * math.pi, (i + 1) * math.pi) for i in range(raw_data['amount']['numbers'])]
            t = 0
            xi1 = []
            xi2 = []
            while t < raw_data['amount']['processes'] * raw_data['step']:
                xi1.append(GRP.model_first_process(t, raw_data['amount']['numbers'], r1, r2))
                xi2.append(GRP.model_second_process(t, raw_data['amount']['numbers'], r1, r2, r3))
                t += raw_data['step']

            processes1.append(xi1)
            processes2.append(xi2)

        print("analyse_processes: part 2")

        means1 = []
        means2 = []
        variance1 = []
        variance2 = []
        for i in range(raw_data['amount']['processes']):
            mean1 = sum(processes1[j][i] for j in range(raw_data['amount']['realizations'])) / raw_data['amount']['realizations']
            means1.append(mean1)
            variance1.append(
                sum((processes1[j][i] - mean1) ** 2 for j in range(raw_data['amount']['realizations'])) / raw_data['amount']['realizations'])

            mean2 = sum(processes2[j][i] for j in range(raw_data['amount']['realizations'])) / raw_data['amount']['realizations']
            means2.append(mean2)
            variance2.append(
                sum((processes2[j][i] - mean2) ** 2 for j in range(raw_data['amount']['realizations'])) / raw_data['amount']['realizations'])

        print("analyse_processes: ready")

        return {
            'first_process': (means1, variance1),
            'second_process': (means2, variance2),
            'first_processes_realizations': (processes1[0], processes1[-1]),
            'second_processes_realizations': (processes2[0], processes2[-1]),
        }