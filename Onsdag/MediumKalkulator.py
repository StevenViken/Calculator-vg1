

from traceback import print_tb

def renter():
    lån = float(input("Lån: ").replace(" ", ""))
    rentefot = float(input("Rentefot: ")) / 100
    år = int(input("År: "))
    rentePerÅr = rentefot / år

    rente = lån * rentePerÅr
    renteHvertÅr = []
    for i in range(int(år)):
        renteHvertÅr.append(rente)
    print(rente)
    return rente, renteHvertÅr

def renterMåneder():
    lån = float(input("Lån: ").replace(" ", ""))
    rentefot = float(input("Rentefot: ")) / 100
    måneder = int(input("Måneder: "))
    rentePerÅr = rentefot / måneder

    rente = lån * rentePerÅr
    renteHverMåned = []
    for i in range(int(måneder)):
        renteHverMåned.append(rente)
    print(rente)
    return rente, renteHverMåned

print(str(renter()) + " kr")
print(str(renterMåneder()) + " kr")