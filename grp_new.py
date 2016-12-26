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

        self.raw_data = None
        self.result_data = None
        self.result = None

        self.makedafault()

        self.chud = ud.CheckHUD(self.alpha.vector, len(self.alpha.vector), self.confidence)

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
            "show image": 12

        }
        pass

    def importparam(self, accuracy):
        self.accuracy = accuracy

    def makedafault(self):
        self.setpath("./")
        self.setfilename("file.xlsx")
        self.setsheetname("Sheet2")
        self.acount = 1000
        self.raw_data = {'amount': {'processes': 200, 'numbers': 100, 'realizations': 100}, 'step': 0.01}

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
        pass

    @staticmethod
    def model_process_1(raw_data):
        xi = []
        for i in range(raw_data['amount']['numbers']):
            eta = 1 / (1 + math.pi * i ** 2)
            arg = i * math.pi * raw_data['t']
            xi.append((math.cos(arg) * raw_data['r1'][i] + math.sin(arg) * raw_data['r2'][i]) * eta)
        return sum(xi)

    @staticmethod
    def model_process_2():
        xi = []
        for i in range(amount_of_numbers):
            eta = 1 / math.sqrt(1 + math.pi * i ** 2) ** 2
            arg = r3[i] * t
            xi.append((math.cos(arg) * r1[i] + math.sin(arg) * r2[i]) * eta)

        return sum(xi)
        pass

    @staticmethod
    def model_process_3():
        pass

    @staticmethod
    def model_process_4():
        pass

    def build_image(self, raw_data, result_data):
        pass

    def sync_data(self):
        pass

    r1 = [math.sqrt(-2 * math.log(random.random())) * math.cos(2 * math.pi * random.random()) for _ in
          range(raw_data['amount']['numbers'])]
    r2 = [math.sqrt(-2 * math.log(random.random())) * math.sin(2 * math.pi * random.random()) for _ in
          range(raw_data['amount']['numbers'])]
    r3 = [random.uniform(i * math.pi, (i + 1) * math.pi) for i in range(raw_data['amount']['numbers'])]