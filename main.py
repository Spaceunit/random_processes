import sys
from scipy.stats import chi2
import matrix
import numpy as np
import openpyxl
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import excel_transfer
import udl
import rvm
import bh
import mgd
import grp
import pfr

class Work:
    def __init__(self):
        self.a = matrix.Matrix([[0]],"Initial matrix")
        self.accuracy = 3
        self.amount_of_numbers = 1
        self.amount_of_intervals = 1
        self.intervals = 1
        self.amount_of_tries = 1
        self.commands = {
            "none": 0,
            "exit": 1,
            "test": 2,
            "clear": 3,
            "help": 4,
            "new": 5,
            "show slist": 6,
            "show scount": 7,
            "acc": 8,
            "mk": 9,
            "udl": 10,
            "rvm": 11,
            "bh": 12,
            "mgd": 13,
            "grp": 14,
            "pfr": 15
        }
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
        print("It is program for lab #1\n",
              "\u2022 enter [udl] to choose task #1\n",
              " \u2023 Description: uniform distribution law\n",
              "\u2022 enter [rvm] to choose task #2\n",
              " \u2023 Description: calculations of Monte Carlo`s integral\n",
              "\u2022 enter [bh] to choose task #3\n",
              " \u2023 Description: building histogram of uniform distribution\n",
              "\u2022 enter [mgd] to choose task #4\n",
              " \u2023 Description: modeling gaussian distribution\n")
        self.showCommands()

    def dostaff(self):
        task = 0
        while (task != 1):
            print('')
            print("Random processes v0.0003 beta task #1")
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
                self.a.showmatrix()
                pass
            elif (task == 8):
                self.setaccuracy()
                pass
            elif (task == 9):
                self.makedafault()
            elif task == 10:
                Lab0 = udl.UDL()
                Lab0.importparam(self.accuracy)
                Lab0.dostaff()
                pass
            elif task == 11:
                Lab0 = rvm.RVM()
                Lab0.importparam(self.accuracy)
                Lab0.dostaff()
                pass
            elif task == 12:
                Lab0 = bh.BH()
                Lab0.importparam(self.accuracy)
                Lab0.dostaff()
                pass
            elif task == 13:
                Lab0 = mgd.MGD()
                Lab0.importparam(self.accuracy)
                Lab0.dostaff()
                pass
            elif task == 14:
                Lab1 = grp.GRP()
                Lab1.importparam(self.accuracy)
                Lab1.dostaff()
                pass
            elif task == 15:
                Lab2 = pfr.PFR()
                Lab2.importparam(self.accuracy)
                Lab2.dostaff()
                pass
        pass

    def inputnewdata0(self):
        task = 0
        self.a = matrix.Matrix([], "Initial matrix")
        while (task != 1):
            print('')
            print("Enter matrix dimension:")
            while (task != 1):
                num = int(input("-> "))
                print("Input is correct? (enter - yes/n - no)")
                command = input("-> ")
                if (command != "n"):
                    self.a = self.inputmatrix(num)
                    task = 1
            task = 0
            self.a.rename("Initial matrix")
            self.a.showmatrix()
            print("Matrix is correct? (enter - yes/n - no)")
            command = input("-> ")
            if (command != "n"):
                task = 1

    def inputmatrix(self, num):
        print('')
        i = 0
        task = 0
        nm = matrix.Matrix([], "new matrix")
        while (i < num):
            print("Enter matrix row (use spaces)")
            print("Row ", i + 1)
            while (task != 1):
                row = list(map(float, input("-> ").split()))
                print("Input is correct? (enter - yes/n - no)")
                command = input("-> ")
                if (command != "n" and len(row) == num):
                    task = 1
                    nm.appendnrow(row)
                elif (len(row) != num):
                    print('')
                    print("Incorrect input: count of items.")
            task = 0
            i += 1
        return nm

    def setaccuracy(self):
        task = 0
        print('')
        print("Enter accuracy:")
        while (task != 1):
            self.accuracy = int(input("-> "))
            print("Input is correct? (enter - yes/n - no)")
            command = input("-> ")
            if (command != "n"):
                task = 1
        pass

    def makedafault(self):
        self.exeldata = excel_transfer.Excel()
        self.a = self.exeldata.transferlist('hvectror')



Some = Work()
Some.dostaff()
