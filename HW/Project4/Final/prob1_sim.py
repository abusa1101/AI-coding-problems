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

tries = 10000
val = []
for i in range(tries):
    val.append(simulate_slots())
mean = sum(val) / float(tries)
n = len(val)
val.sort()
if n % 2 == 0:
    median1 = val[n//2]
    median2 = val[n//2 - 1]
    median = (median1 + median2)/2
else:
    median = val[n//2]

print("Tries, Mean, Median: %s, %s, %s" % (tries, mean, median))
