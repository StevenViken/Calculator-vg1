
from numpy import kron


def bigMoney(days):
    dailyIncrease = 1.15
    kroner = 300
    moneys = kroner
    for i in range(days - 1):
        kroner = kroner * dailyIncrease
        moneys = moneys + kroner
    print("Lønn på dag " + str(days) + " er " + str(kroner) + " kr.")
    return moneys

bigMoney(15)
bigMoney(30)
bigMoney(45)
bigMoney(50)
print("Total lønn etter 2 månder er " + str(bigMoney(60)) + " kr.")