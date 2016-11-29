import openpyxl
import matrix
import numpy as np
import uniform_distribution as ud
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import excel_transfer

class UDL:
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
            "new intervals": 11

        }
        pass

    def importparam(self, accuracy):
        self.accuracy = accuracy

    def makedafault(self):
        self.setpath("./")
        self.setfilename("file.xlsx")
        self.setsheetname("Sheet1")
        self.confidence = 0.95
        self.alphas_count = 1000
        self.amount_of_intervals = 10


        # alpha in numpy format of array
        self.anp = np.random.sample(self.alphas_count)
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
            print("Uniform distribution law (task1) v0.0001 beta task #5")
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
            elif (task == 11):
                self.input_new_count_of_intervals()
                pass
        pass

    def inputnewdata(self):
        task = 0
        print('')
        print("Enter count of alphas (numbers, default 1000):")
        while (task != 1):
            self.alphas_count = int(input("-> "))
            print("Input is correct? (enter - yes/n - no)")
            command = input("-> ")
            if (command != "n"):
                task = 1

    def input_new_count_of_intervals(self):
        task = 0
        print('')
        print("Enter count of intervals (numbers, default 10):")
        while (task != 1):
            self.alphas_count = int(input("-> "))
            print("Input is correct? (enter - yes/n - no)")
            command = input("-> ")
            if (command != "n"):
                task = 1

    def input_new_confidence(self):
        task = 0
        print('')
        print("Enter confidence (default 0.95):")
        while (task != 1):
            self.amount_of_intervals = float(input("-> "))
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
        print("Confidence:", self.confidence)
        print("Chi-squared:", self.chi_squared)
        print("Critical value:", self.critical_value)
        print("P-value:", self.p_value)
        print("Result:", self.result)

        #print("Data array:", self.data_array)

    def generate_random_numbers(self):
        #Here we will generate random numbers
        self.data_array = self.chud.generate_random_numbers([0.0, 1.0], self.alphas_count)
        pass

    def transferlist(self):
        self.exeldata = excel_transfer.Excel()
        self.alpha = self.exeldata.transferlist('hvectror')


    def resolve(self):
        self.generate_random_numbers()
        self.show_present_data()
        self.result_data = self.chud.checkHUD(self.data_array, self.amount_of_intervals, self.confidence)
        self.sync_data()
        self.show_present_data()
        self.printresult()
        pass

    def sync_data(self):
        self.chi_squared = self.result_data['chi_sq']
        self.critical_value = self.result_data['critical']
        self.p_value = self.result_data['p_value']