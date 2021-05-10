import random as rd

def simulate_slots():
    play_num = 0
    balance = 10
    cherry_payback = 0

    while balance:
        balance -= 1
        play_num += 1
        symbols = ["bar", "bell", "lemon", "cherry", "blank", "blank", "blank", "blank"]

        wheels = []
        for i in range(3):
            wheels.append(rd.choice(symbols))

        if wheels[0] == "cherry":
            if wheels[0] == wheels[1]:
                if wheels[1] == wheels[2]:
                    cherry_payback = 3
                else:
                    cherry_payback = 2
            else:
                cherry_payback = 1
            balance += cherry_payback
        elif wheels[0] == wheels[1] and wheels[1] == wheels[2]:
            if wheels[0] == "bar":
                balance += 20
            elif wheels[0] == "bell":
                balance += 15
            elif wheels[0] == "lemon":
                balance += 5
            else:
                balance += 0
    return play_num

TRIES = 10000
VAL = []
for x in range(TRIES):
    VAL.append(simulate_slots())
MEAN = sum(VAL) / float(TRIES)
N = len(VAL)
VAL.sort()
if N % 2 == 0:
    MEDIAN1 = VAL[N//2]
    MEDIAN2 = VAL[N//2 - 1]
    MEDIAN = (MEDIAN1 + MEDIAN2)/2
else:
    MEDIAN = VAL[N//2]

print("Tries, Mean, Median: %s, %s, %s" % (TRIES, MEAN, MEDIAN))
