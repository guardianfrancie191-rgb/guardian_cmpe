
import math



def get_inductor_value_of_material(relativeP, permeability, turns, area, length):
    inductance = (relativeP * permeability * turns * area)/ length
    print (f"The inductor value is {inductance}")
    return inductance


def get_inductive_reactance(frequency, inductance):
    reactance = 2 * math.pi * frequency * inductance
    print ("Inductive reactance is:" + str(reactance) + " ohms")
    return reactance

if __name__ == "__main__":
    get_inductive_reactance(frequency, inductance)


