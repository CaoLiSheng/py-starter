class FunktionsDeklarationError(ImportError):
  pass

import ast
import math
from sys import argv
try:
  from co2_PA04solution import *
except ImportError:
  raise FunktionsDeklarationError('Fehler.')


def takeSecond(elem):
    return elem[1]

def takeFirst(elem):
    return elem[0]

def _GlobalUnion(P):
    elements = []
    for a in P.Sets: elements += a.Elements()
    elements.sort(key=takeSecond)
    elements.sort(key=takeFirst)
    return elements

def _CheckRep(P):
    elts = _GlobalUnion(P)
    for i in elts:
        if P.FindSet(i)!= P.FindSet(P.FindSet(i)):
            print ("Representatives: line " + count + " wrong")
            
def _AddTail(P):
	P.MakeSet((500,500))
	P.MakeSet((500,501))
	P.MakeSet((501,501))
	P.MakeSet((1500,1500))
	P.MakeSet((1500,1501))
	P.MakeSet((1501,1501))
	
def _TestUnion(P):
	P.Union
	P.Union((500,500),(500,501))
	P.Union((500,500),(501,501))
	P.Union((500,500),(1500,1500))
	P.Union((500,500),(1500,1501))
	P.Union((500,500),(1501,1501))

def _CheckExceptionMakeSet(P):
    try:
        P.MakeSet((500,500))		
    except Exception as inst:
        if (inst.args[0] == "invalid operation"): print("Error OK.")
        
def _CheckExceptionFindSet(P):
    try:
        P.FindSet((2500,2500))		
    except Exception as inst:
        if (inst.args[0] == "invalid operation"): print("Error OK.")

#with open(argv[1],'r') as f:
with open('private_std.in','r') as f:
    for line in f:
        l = ast.literal_eval(line)
        #initialisiert Objekt
        P = Partition(l)
        #druckt Liste aller Set-Elemente (die je nur ein 
        #Tupel in _elements enthalten) in Sets
        print(_GlobalUnion(P))
        #fugt Sets eine Reihe von Set-Objekten 
        _AddTail(P)
        #druckt wiederum Liste aller Set-Objekte
        print(_GlobalUnion(P))
        #uberpruft die wichtigsten Exceptions
        _CheckExceptionMakeSet(P)
        _CheckExceptionFindSet(P)
        #testet Union-Funktion
        _TestUnion(P)
        #testet Findset
        print(P.FindSet((1500,1500)))
        
        print("\n------------------------------------------------------------------------\n")

        
        
        
        
        
        
