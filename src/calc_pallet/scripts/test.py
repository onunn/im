#!/usr/bin/env python
import rospy
from std_msgs.msg import String

from ortools.sat.python import cp_model

import sys

class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
    result = ''

    """Print intermediate solutions."""
    def __init__(self, variables):

        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables

    def on_solution_callback(self):
        for v in self.__variables:
            VarArraySolutionPrinter.result += ('%s=%i, ' %(v, self.Value(v)))
        VarArraySolutionPrinter.result += "\n"

    def printf(self):
        print(VarArraySolutionPrinter.result)

def SolveSat(maxX1, maxX2, maxX3):
    model = cp_model.CpModel()
    
    Result = []
    
    X1 = model.NewIntVar(0, maxX1, "X1")
    X2 = model.NewIntVar(0, maxX2, "X2")
    X3 = model.NewIntVar(0, maxX3, "X3")
    b = model.NewBoolVar('b')
    
    model.Add(X1 <= maxX1).OnlyEnforceIf(b)
    model.Add(X1 > maxX1).OnlyEnforceIf(b.Not())
    model.Add(X2 <= maxX2).OnlyEnforceIf(b)
    model.Add(X2 > maxX2).OnlyEnforceIf(b.Not())
    model.Add(X3 <= maxX3).OnlyEnforceIf(b)
    model.Add(X2 > maxX2).OnlyEnforceIf(b.Not())
    
    model.Add(960*X1 + 480*X2 + 240*X3 == 5760)
    model.AddDecisionStrategy([X1, X2, X3], cp_model.CHOOSE_FIRST, cp_model.SELECT_MIN_VALUE)
    
    solver = cp_model.CpSolver()
    
    solution_printer = VarArraySolutionPrinter([X1, X2, X3])
    
    solver.SearchForAllSolutions(model, solution_printer)
    
    solution_printer.printf()

def StringToListProcess(string):
    string.strip()
    boxCanAlign = []
    oneLayer = []

    while string.find('\n') != -1:
        lineAlignPosition = string.find('\n')
    
        oneLayerString = string[:lineAlignPosition]
        string = string[lineAlignPosition+1:]
        
        while oneLayerString.find(',') != -1:
            CommaPosition = oneLayerString.find(',')
            oneLayer.append(oneLayerString[:CommaPosition])
            oneLayerString = oneLayerString[CommaPosition+2:]

        boxCanAlign.append(oneLayer)
        oneLayer = []

    return boxCanAlign

def stringListToList(string):    
    leftBracketPos = string.find("[")
    rightBracketPos = string.find("]")
    
    string = string[leftBracketPos+1:rightBracketPos]
    returnList = map(int, string.split(','))

    return returnList

def callback(data):
    Data = stringListToList(data.data)
    
    print(Data)

    maxX1 = Data[0]
    maxX2 = Data[1]
    maxX3 = Data[2]
    

    #SolveSat(maxX1, maxX2, maxX3)

def listener():
    rospy.init_node('selectBox', anonymous=True)
    rospy.Subscriber('/box_List', String, callback)
    
    rospy.spin()

if __name__ == '__main__':
    listener()
