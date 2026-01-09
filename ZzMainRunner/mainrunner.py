


from Capacitor import Capacitance
from Resistor import resistance
from Inductor   import Inductance

while True:

        selector = input("Please select calculator: ")

        match selector.upper():
            case "CC_CV":
                print("Capacitance Calculator")
                charge = float(input("Enter the charge : "))
                voltage = float(input("Enter the voltage : "))
                Capacitance.get_capacitance_by_CV(charge, voltage)

            case "R_OHM":
                print ("Resistance Calculator OHMS LAW")
                current = float(input("Enter the current : "))
                voltage = float(input("Enter the voltage : "))
                resistance.get_resistance_by_ohms_law(voltage, current)

            case "L_REACT":
                print("Inductor Resistance Calculator")
                frequency = float(input("Enter the frequency : "))
                inductance = float(input("Enter the inductance : "))
                Inductance.get_inductive_reactance(frequency, inductance)