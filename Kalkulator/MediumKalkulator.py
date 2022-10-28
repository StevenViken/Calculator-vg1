import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

Lånebeløp = float(input("Lånebeløp: ").replace(" ", ""))
Løpetid = int(input("Løpetid i år: ").replace(" ", ""))
Terminer = int(input("Terminer per år: ").replace(" ", ""))
Rente = float(input("Rente %: ").replace(" ", ""))/100
Avdrag = Lånebeløp / (Løpetid*Terminer)

numberList = []

Restlån = Lånebeløp
Renter = 0
TerminBeløp = 0

listRestlån = []
listAvdrag = []
listRenter = []
listTerminBeløp = []


for i in range(Løpetid * Terminer):
    numberList.append(i+1)
    if i != 0:
        Restlån = Restlån - Avdrag
    listRestlån.append(Restlån)
    Renter = Restlån * Rente
    listRenter.append(Renter)
    listAvdrag.append(Avdrag)
    listTerminBeløp.append(Renter+Avdrag)


data = pd.DataFrame({"Restlån": listRestlån, "Avdrag": listAvdrag, "Renter": listRenter, "Termin Beløp": listTerminBeløp})
print(data)

width = 0.35

fig, ax = plt.subplots()

ax.bar(numberList, listAvdrag, width, label='Avdrag')
ax.bar(numberList, listRenter, width, bottom=listAvdrag,
       label='Renter')

plt.ticklabel_format(style='plain')

ax.set_ylabel('Kroner')
ax.set_xlabel('Terminer')
ax.set_title('Renter og avdrag')
ax.legend()
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.yaxis.set_major_formatter('{x:1.2f} kr')

plt.show()