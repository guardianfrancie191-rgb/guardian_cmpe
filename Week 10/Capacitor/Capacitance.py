
import math


#ErEo(A/d)
def get_capacitance_by_material(Permeability, Area, Distance):
    dielectricCon = 8.854 * 10e-12 #F/n
    Capacitance = (Permeability + dielectricCon * Area) /Distance
    print (f" Capacitance of Material is : {Capacitance}")
    return Capacitance


def get_capacitance_by_CV(Charge, Voltage):
    Capacitance = Charge / Voltage
    print (f"Capacitance by CV: {Capacitance} Farad")
    return Capacitance


def get_capacitance_current(capacitance, dvoverdt):
    ic = capacitance * dvoverdt
    print (f"Capacitor Current: {ic}")
    return ic

def get_capacitive_reactance(frequency, capacitance):
    reactance = 1 / (2 * math.pi * frequency * capacitance)
    print ("Capacitive reactance is ", reactance)
    return reactance


if __name__ == "__main__":
    get_capacitance_by_CV()


