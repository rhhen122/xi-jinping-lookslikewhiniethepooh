from info import name #type: ignore
from info import author #type: ignore
from info import maintainer #type: ignore
from info import version #type: ignore
from info import readme #type: ignore
import os #type: ignore
def many(): #type: ignore
    print("NAME: " + name) #type: ignore
    print("AUTHOR: " + author) #type: ignore
    print("MAINTAINER: " + maintainer) #type: ignore
    print("VERSION: " + version) #type: ignore
    print("README: ") #type: ignore
    os.system(readme) #type: ignore
def start(ver): #type: ignore
    print("scrap: " + ver) #type: ignore
    print("scrap: know") #type: ignore
    print("scrap: live") #type: ignore
start("1") #type: ignore
startopen = input("Press ENTER/RETURN to continue!") #type: ignore
if startopen == (""): #type: ignore
    many() #type: ignore
else: #type: ignore
    print("Error!") #type: ignore
