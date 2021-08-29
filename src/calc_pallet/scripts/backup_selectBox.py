#!/usr/bin/env python
import rospy
from std_msgs.msg import String

from ortools.linear_solver import pywraplp
from ortools.sat.python import cp_model
import sys


class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
    """Print intermediate solutions."""
    result = ''

    def __init__(self, variables):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables

    def on_solution_callback(self):
        for v in self.__variables:
            VarArraySolutionPrinter.result += ('%s=%i, ' %(v, self.Value(v)))
        VarArraySolutionPrinter.result += "\n"

    def returnString(self):
         return VarArraySolutionPrinter.result

def SolvePossibleBoxSet(maxX1, maxX2, maxX3):
    model = cp_model.CpModel()

    #Result = []

    #maxX1 : 16x8 maxX2 : 8x8 maxX3 : 8x4

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

    model.Add(128*X1 + 64*X2 + 32*X3 == 768)

    model.AddDecisionStrategy([X1, X2, X3], cp_model.CHOOSE_FIRST, cp_model.SELECT_MIN_VALUE)

    solver = cp_model.CpSolver()

    solution_printer = VarArraySolutionPrinter([X1, X2, X3])
    
    solver.SearchForAllSolutions(model, solution_printer)
    selectBox.result = solution_printer.returnString()

def ProcessStringToList(string):
    string.strip()
    boxCanAlign = []
    oneLayer = []

    while string.find('\n') != -1:
        lineAlignPosition = string.find('\n')

        oneLayerString = string[:lineAlignPosition]
        string = string[lineAlignPosition+1:]


        while oneLayerString.find('=') != -1:
            CommaPosition = oneLayerString.find(',')
            EqualPosition = oneLayerString.find('=')
            oneLayer.append(int(oneLayerString[EqualPosition+1:EqualPosition+2]))
            oneLayerString = oneLayerString[CommaPosition+2:]

        boxCanAlign.append(oneLayer)
        oneLayer = []

    return boxCanAlign

def SelectBoxCount(boxCanAlign):
    boxCanAlign.sort()
    boxCanAlign.reverse()

    return boxCanAlign[0]

def SolveEachLayerSet(X1, X2, X3):

    solver = pywraplp.Solver('SolveSimpleSystem', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

    x11 = solver.NumVar(0, solver.infinity(), "x11")
    x12 = solver.NumVar(0, solver.infinity(), "x12")
    x13 = solver.NumVar(0, solver.infinity(), "x13")
    x21 = solver.NumVar(0, solver.infinity(), "x21")
    x22 = solver.NumVar(0, solver.infinity(), "x22")
    x23 = solver.NumVar(0, solver.infinity(), "x23")
    x31 = solver.NumVar(0, solver.infinity(), "x31")
    x32 = solver.NumVar(0, solver.infinity(), "x32")
    x33 = solver.NumVar(0, solver.infinity(), "x33")
    x41 = solver.NumVar(0, solver.infinity(), "x41")
    x42 = solver.NumVar(0, solver.infinity(), "x42")
    x43 = solver.NumVar(0, solver.infinity(), "x43")
    x51 = solver.NumVar(0, solver.infinity(), "x51")
    x52 = solver.NumVar(0, solver.infinity(), "x52")
    x53 = solver.NumVar(0, solver.infinity(), "x53")
    x61 = solver.NumVar(0, solver.infinity(), "x61")
    x62 = solver.NumVar(0, solver.infinity(), "x62")
    x63 = solver.NumVar(0, solver.infinity(), "x63")

    a1 = solver.NumVar(0, solver.infinity(), "a1")
    a2 = solver.NumVar(0, solver.infinity(), "a2")
    a3 = solver.NumVar(0, solver.infinity(), "a3")
    b1 = solver.NumVar(0, solver.infinity(), "b1")
    b2 = solver.NumVar(0, solver.infinity(), "b2")
    b3 = solver.NumVar(0, solver.infinity(), "b3")
    c1 = solver.NumVar(0, solver.infinity(), "c1")
    c2 = solver.NumVar(0, solver.infinity(), "c2")
    c3 = solver.NumVar(0, solver.infinity(), "c3")
    d1 = solver.NumVar(0, solver.infinity(), "d1")
    d2 = solver.NumVar(0, solver.infinity(), "d2")
    d3 = solver.NumVar(0, solver.infinity(), "d3")
    e1 = solver.NumVar(0, solver.infinity(), "e1")
    e2 = solver.NumVar(0, solver.infinity(), "e2")
    e3 = solver.NumVar(0, solver.infinity(), "e3")
    f1 = solver.NumVar(0, solver.infinity(), "f1")
    f2 = solver.NumVar(0, solver.infinity(), "f2")
    f3 = solver.NumVar(0, solver.infinity(), "f3")
    g1 = solver.NumVar(0, solver.infinity(), "g1")
    g2 = solver.NumVar(0, solver.infinity(), "g2")
    g3 = solver.NumVar(0, solver.infinity(), "g3")
    h1 = solver.NumVar(0, solver.infinity(), "h1")
    h2 = solver.NumVar(0, solver.infinity(), "h2")
    h3 = solver.NumVar(0, solver.infinity(), "h3")
    i1 = solver.NumVar(0, solver.infinity(), "i1")
    i2 = solver.NumVar(0, solver.infinity(), "i2")
    i3 = solver.NumVar(0, solver.infinity(), "i3")

    z = solver.NumVar(0, solver.infinity(), "z")
    y = solver.NumVar(0, solver.infinity(), "y")

    P = 16*16 
    W = 16
    #L = 16

    A = 16*8
    B = 8*8
    C = 8*4


    objective = solver.Objective()
    objective.SetCoefficient(x11, A)
    objective.SetCoefficient(x12, A)
    objective.SetCoefficient(x13, A)
    objective.SetCoefficient(x21, A)
    objective.SetCoefficient(x22, A)
    objective.SetCoefficient(x23, A)
    objective.SetCoefficient(x31, B)
    objective.SetCoefficient(x32, B)
    objective.SetCoefficient(x33, B)
    objective.SetCoefficient(x41, B)
    objective.SetCoefficient(x42, B)
    objective.SetCoefficient(x43, B)
    objective.SetCoefficient(x51, C)
    objective.SetCoefficient(x52, C)
    objective.SetCoefficient(x53, C)
    objective.SetCoefficient(x61, C)
    objective.SetCoefficient(x62, C)
    objective.SetCoefficient(x63, C)
    objective.SetCoefficient(z, 1)
    objective.SetCoefficient(y, -1)


    objective.SetMaximization()

    constraint = solver.Constraint(-solver.infinity(), X1)
    constraint.SetCoefficient(x11, 1)
    constraint.SetCoefficient(x21, 1)
    constraint.SetCoefficient(x12, 1)
    constraint.SetCoefficient(x22, 1)
    constraint.SetCoefficient(x13, 1)
    constraint.SetCoefficient(x23, 1)

    constraint = solver.Constraint(-solver.infinity(), X2)
    constraint.SetCoefficient(x31, 1)
    constraint.SetCoefficient(x41, 1)
    constraint.SetCoefficient(x32, 1)
    constraint.SetCoefficient(x42, 1)
    constraint.SetCoefficient(x33, 1)
    constraint.SetCoefficient(x43, 1)

    constraint = solver.Constraint(-solver.infinity(), X3)
    constraint.SetCoefficient(x51, 1)
    constraint.SetCoefficient(x61, 1)
    constraint.SetCoefficient(x52, 1)
    constraint.SetCoefficient(x62, 1)
    constraint.SetCoefficient(x53, 1)
    constraint.SetCoefficient(x63, 1)

    constraint = solver.Constraint(-solver.infinity(),P)
    constraint.SetCoefficient(x11, A)
    constraint.SetCoefficient(x21, A)
    constraint.SetCoefficient(x31, B)
    constraint.SetCoefficient(x41, B)
    constraint.SetCoefficient(x51, C)
    constraint.SetCoefficient(x61, C)

    constraint = solver.Constraint(-solver.infinity(),P)
    constraint.SetCoefficient(x12, A)
    constraint.SetCoefficient(x22, A)
    constraint.SetCoefficient(x32, B)
    constraint.SetCoefficient(x42, B)
    constraint.SetCoefficient(x52, C)
    constraint.SetCoefficient(x62, C)

    constraint = solver.Constraint(-solver.infinity(),P)
    constraint.SetCoefficient(x13, A)
    constraint.SetCoefficient(x23, A)
    constraint.SetCoefficient(x33, B)
    constraint.SetCoefficient(x43, B)
    constraint.SetCoefficient(x53, C)
    constraint.SetCoefficient(x63, C)

    constraint = solver.Constraint(-solver.infinity(),W)
    constraint.SetCoefficient(a1, 1)
    constraint.SetCoefficient(b1, 1)
    constraint.SetCoefficient(c1, 1)
    constraint.SetCoefficient(d1, 1)
    constraint.SetCoefficient(e1, 1)
    constraint.SetCoefficient(f1, 1)
    constraint.SetCoefficient(g1, 1)
    constraint.SetCoefficient(h1, 1)
    constraint.SetCoefficient(i1, 1)

    constraint = solver.Constraint(-solver.infinity(),W)
    constraint.SetCoefficient(a2, 1)
    constraint.SetCoefficient(b2, 1)
    constraint.SetCoefficient(c2, 1)
    constraint.SetCoefficient(d2, 1)
    constraint.SetCoefficient(e2, 1)
    constraint.SetCoefficient(f2, 1)
    constraint.SetCoefficient(g2, 1)
    constraint.SetCoefficient(h2, 1)
    constraint.SetCoefficient(i2, 1)

    constraint = solver.Constraint(-solver.infinity(),W)
    constraint.SetCoefficient(a3, 1)
    constraint.SetCoefficient(b3, 1)
    constraint.SetCoefficient(c3, 1)
    constraint.SetCoefficient(d3, 1)
    constraint.SetCoefficient(e3, 1)
    constraint.SetCoefficient(f3, 1)
    constraint.SetCoefficient(g3, 1)
    constraint.SetCoefficient(h3, 1)
    constraint.SetCoefficient(i3, 1)

    constraint = solver.Constraint(0,solver.infinity())
    constraint.SetCoefficient(x61, -8)
    constraint.SetCoefficient(c1, 2)
    constraint.SetCoefficient(d1, 1)
    constraint.SetCoefficient(f1, 4)
    constraint.SetCoefficient(g1, 3)
    constraint.SetCoefficient(h1, 2)
    constraint.SetCoefficient(i1, 1)

    constraint = solver.Constraint(0,solver.infinity())
    constraint.SetCoefficient(x62, -8)
    constraint.SetCoefficient(c2, 2)
    constraint.SetCoefficient(d2, 1)
    constraint.SetCoefficient(f2, 4)
    constraint.SetCoefficient(g2, 3)
    constraint.SetCoefficient(h2, 2)
    constraint.SetCoefficient(i2, 1)

    constraint = solver.Constraint(0,solver.infinity())
    constraint.SetCoefficient(x63, -8)
    constraint.SetCoefficient(c3, 2)
    constraint.SetCoefficient(d3, 1)
    constraint.SetCoefficient(f3, 4)
    constraint.SetCoefficient(g3, 3)
    constraint.SetCoefficient(h3, 2)
    constraint.SetCoefficient(i3, 1)


    constraint = solver.Constraint(0,solver.infinity())
    constraint.SetCoefficient(x21, -16)
    constraint.SetCoefficient(x31, -8)
    constraint.SetCoefficient(x41, -8)
    constraint.SetCoefficient(x51, -4)
    constraint.SetCoefficient(b1, 2)
    constraint.SetCoefficient(c1, 1)
    constraint.SetCoefficient(d1, 1)
    constraint.SetCoefficient(e1, 1)

    constraint = solver.Constraint(0,solver.infinity())
    constraint.SetCoefficient(x22, -16)
    constraint.SetCoefficient(x32, -8)
    constraint.SetCoefficient(x42, -8)
    constraint.SetCoefficient(x52, -4)
    constraint.SetCoefficient(b2, 2)
    constraint.SetCoefficient(c2, 1)
    constraint.SetCoefficient(d2, 1)
    constraint.SetCoefficient(e2, 1)

    constraint = solver.Constraint(0,solver.infinity())
    constraint.SetCoefficient(x23, -16)
    constraint.SetCoefficient(x33, -8)
    constraint.SetCoefficient(x43, -8)
    constraint.SetCoefficient(x53, -4)
    constraint.SetCoefficient(b3, 2)
    constraint.SetCoefficient(c3, 1)
    constraint.SetCoefficient(d3, 1)
    constraint.SetCoefficient(e3, 1)

    constraint.SetCoefficient(x11, -8)
    constraint.SetCoefficient(a1, 1)

    constraint = solver.Constraint(0,solver.infinity())
    constraint.SetCoefficient(x12, -8)
    constraint.SetCoefficient(a2, 1)

    constraint = solver.Constraint(0,solver.infinity())
    constraint.SetCoefficient(x13, -8)
    constraint.SetCoefficient(a3, 1)

    constraint = solver.Constraint(-solver.infinity(), 0)
    constraint.SetCoefficient(x11, 1)
    constraint.SetCoefficient(x21, 1)
    constraint.SetCoefficient(x31, 1)
    constraint.SetCoefficient(x41, 1)
    constraint.SetCoefficient(x51, 1)
    constraint.SetCoefficient(x61, 1)
    constraint.SetCoefficient(x12, -1)
    constraint.SetCoefficient(x22, -1)
    constraint.SetCoefficient(x32, -1)
    constraint.SetCoefficient(x42, -1)
    constraint.SetCoefficient(x52, -1)
    constraint.SetCoefficient(x62, -1)

    constraint = solver.Constraint(-solver.infinity(), 0)
    constraint.SetCoefficient(x12, 1)
    constraint.SetCoefficient(x22, 1)
    constraint.SetCoefficient(x32, 1)
    constraint.SetCoefficient(x42, 1)
    constraint.SetCoefficient(x52, 1)
    constraint.SetCoefficient(x62, 1)
    constraint.SetCoefficient(x13, -1)
    constraint.SetCoefficient(x23, -1)
    constraint.SetCoefficient(x33, -1)
    constraint.SetCoefficient(x43, -1)
    constraint.SetCoefficient(x53, -1)
    constraint.SetCoefficient(x63, -1)

    constraint = solver.Constraint(0, solver.infinity())
    constraint.SetCoefficient(x11, A)
    constraint.SetCoefficient(x21, A)
    constraint.SetCoefficient(x31, B)
    constraint.SetCoefficient(x41, B)
    constraint.SetCoefficient(x51, C)
    constraint.SetCoefficient(x61, C)
    constraint.SetCoefficient(x12, -A)
    constraint.SetCoefficient(x22, -A)
    constraint.SetCoefficient(x32, -B)
    constraint.SetCoefficient(x42, -B)
    constraint.SetCoefficient(x52, -C)
    constraint.SetCoefficient(x62, -C)

    constraint = solver.Constraint(0, solver.infinity())
    constraint.SetCoefficient(x12, A)
    constraint.SetCoefficient(x22, A)
    constraint.SetCoefficient(x32, B)
    constraint.SetCoefficient(x42, B)
    constraint.SetCoefficient(x52, C)
    constraint.SetCoefficient(x62, C)
    constraint.SetCoefficient(x13, -A)
    constraint.SetCoefficient(x23, -A)
    constraint.SetCoefficient(x33, -B)
    constraint.SetCoefficient(x43, -B)
    constraint.SetCoefficient(x53, -C)
    constraint.SetCoefficient(x63, -C)

    constraint = solver.Constraint(0, 0)
    constraint.SetCoefficient(x13, 1)
    constraint.SetCoefficient(x23, 1)
    constraint.SetCoefficient(x33, 1)
    constraint.SetCoefficient(x43, 1)
    constraint.SetCoefficient(x53, 1)
    constraint.SetCoefficient(x63, 1)
    constraint.SetCoefficient(z, -1)

    constraint = solver.Constraint(0, 0)
    constraint.SetCoefficient(x11, 1)
    constraint.SetCoefficient(x21, 1)
    constraint.SetCoefficient(x31, 1)
    constraint.SetCoefficient(x41, 1)
    constraint.SetCoefficient(x51, 1)
    constraint.SetCoefficient(x61, 1)
    constraint.SetCoefficient(y, -1)

    solver.Solve()

    layer1 = [x11, x21, x31, x41, x51, x61, x12, x22, x32, x42, x52, x62, x13, x23, x33, x43, x53, x63]

    list1 = [a1, b1, c1, d1, e1, f1, g1, h1, i1,
            a2, b2, c2, d2, e2, f2, g2, h2, i2,
            a3, b3, c3, d3, e3, f3, g3, h3, i3]

    #lengthSet = {'a': '24,24', 'b': '24,24'},

    box_usedType = []
    layer_width = []
    for i in layer1:
        if abs(round(i.solution_value())) != 0:
            #print("{} : ".format(i), abs(round(i.solution_value())))
            box_usedType.append((i,abs(round(i.solution_value()))))


    for i in list1:
        if abs(round(i.solution_value())) != 0:
            #print("{} : ".format(i), abs(round(i.solution_value())))
            layer_width.append((i,abs(round(i.solution_value()))))

    print(box_usedType)
    print(layer_width)

class selectBox:
    result = ''
    X1 = 0
    X2 = 0
    X3 = 0

    def __init__(self):
        self.Subscriber = rospy.Subscriber("/box_List", String, self.callback)

    def callback(self, data):
        Data = data.data
        returnList = stringListToList(Data)
        
        selectBox.X1 = returnList[0]
        selectBox.X2 = returnList[1]
        selectBox.X3 = returnList[2]
        
        print("X1 : {}, X2 : {}, X3 : {}\n".format(selectBox.X1,selectBox.X2, selectBox.X3))


        SolvePossibleBoxSet(selectBox.X1, selectBox.X2, selectBox.X3)
        print(selectBox.result)

        boxCanAlign = ProcessStringToList(selectBox.result)
        boxCanAlign = SelectBoxCount(boxCanAlign)

        print("===========Box Can Align============")
        print(boxCanAlign)
        print("====================================")
        SolveEachLayerSet(boxCanAlign[0],boxCanAlign[1],boxCanAlign[2])



def stringListToList(string):    
    leftBracketPos = string.find("[")
    rightBracketPos = string.find("]")
    
    string = string[leftBracketPos+1:rightBracketPos]
    returnList = map(int, string.split(','))

    return returnList

def main(args):
    ic = selectBox()
    rospy.init_node('selectBox', anonymous=True)

    try:
        rospy.spin()

    except KeyboardInterrupt:
        print "Shutting Down ROS Image Feature Detector Module"


if __name__ == "__main__":
    print("================================")
    print("start selectBox node")
    print("================================")

    main(sys.argv)
