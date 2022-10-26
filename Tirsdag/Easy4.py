seat_number = []

while True:
    seat_number.append(0)
    for i in range(50):
        seat_number.append(i + 1)
    seatNum = 0
    for i in range(len(seat_number)):
        seatNum = seatNum + seat_number[i]
    print(seatNum)
    break
    