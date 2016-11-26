import openpyxl
import math
import matrix
import numpy as np
import uniform_distribution as ud
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import excel_transfer
import calc_integral_monte_carlo

class RVM:
    def __init__(self):
        self.alpha = matrix.Vector([], "Initial vectror")
        self.arnum = matrix.Vector([], "Array of random numbers")
        self.a = matrix.Matrix([[0]], "Initial matrix")
        #In this case data_array is array of random numbers
        self.data_array = matrix.Vector([], "Array of our data :)")
        self.amount_of_intervals = 1
        self.confidence = 0.95
        self.chi_squared = None
        self.critical_value = None
        self.p_value = None
        self.result = None

        self.makedafault()

        self.chud = ud.CheckHUD(self.alpha.vector, len(self.alpha.vector), self.confidence)
        self.cimc = calc_integral_monte_carlo.MCintegral()

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
            "exp list": 11

        }
        pass

    def importparam(self, accuracy):
        self.accuracy = accuracy

    def makedafault(self):
        self.setpath("./")
        self.setfilename("file.xlsx")
        self.setsheetname("Sheet2")
        self.acount = 1000
        self.amount_of_intervals = 10

        self.result = {}

        self.result['integral1'] = {}
        self.result['integral2'] = {}
        self.result['integral3'] = {}

        self.result['integral1']['expression'] = 'x**7 + x**5 + x**3'
        self.result['integral1']['boundary'] = (0, 1)

        self.result['integral2']['expression'] = '2 * sin(3*x)'
        self.result['integral2']['boundary'] = (0, math.pi)

        self.result['integral3']['expression'] = '1 / ((x + 1) * sqrt(x))'
        self.result['integral3']['boundary'] = (0, 100000)


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
            print("Computing by Monte Carlo`s method (task2) v0.0002 beta task #5")
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
                self.show_expression_list()
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
        #print(self.result_data)
        count, bins, ignored = plt.hist(self.data_array, self.amount_of_intervals, normed=True)
        plt.plot(bins, np.ones_like(bins), linewidth=2, color='r')
        plt.show()
        pass

    def show_present_data(self):
        print("Present data:")
        print("Amount of intervals:", self.amount_of_intervals)
        print("x\u005E7 + x\u005E5 + x\u005E3:", self.result['integral1']['result'])
        print("2\u00D7sin(3\u00D7x):", self.result['integral2']['result'])
        print("1\u00F7((x + 1)\u00D7(x)\u005E(\u00BD)):", self.result['integral3']['result'])
        #
        # print("Data array:", self.data_array)

    def generate_random_numbers(self):
        #Here we will generate random numbers
        self.data_array = self.chud.generate_random_numbers([0.0, 1.0], self.acount)
        pass

    def transferlist(self):
        self.exeldata = excel_transfer.Excel()
        self.alpha = self.exeldata.transferlist('hvectror')


    def resolve(self):
        self.generate_random_numbers()
        #self.show_present_data()
        # self.result_data = self.chud.checkHUD(self.data_array, self.amount_of_intervals, self.confidence)
        # self.sync_data()

        self.count_integral('integral1', self.amount_of_intervals)
        self.count_integral('integral2', self.amount_of_intervals)
        self.count_integral('integral3', self.amount_of_intervals * 5000)

        self.show_present_data()
        # self.printresult()
        pass

    def sync_data(self):
        self.chi_squared = self.result_data['chi_sq']
        self.critical_value = self.result_data['critical']
        self.p_value = self.result_data['p_value']

    def count_integral(self, expression_name, amount_of_intervals):
        intervals = amount_of_intervals
        expression = self.result[expression_name]['expression']
        boundary = self.result[expression_name]['boundary']
        self.result[expression_name]['result'] = self.cimc.count(expression=expression, boundary=boundary, amount_of_intervals=intervals)

    def show_expression_list(self):
        print('Expresson list')
        print('')
        print(self.result)
        for i in range(len(self.result)):
            print(self.result["integral" + str(i + 1)])
# 'x**7 + x**5 + x**3' [0,1]
# '2 * sin(3*x)' [0, math.pi]
# '1 / ((x + 1) * sqrt(x))' [0, 100000] amount_of_intervals = amount_of_intervals * 5000
# \u00D7
# \u00BD 1/2