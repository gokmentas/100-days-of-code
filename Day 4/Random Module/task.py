import random

heads_count = 0
tails_count = 0
i = 0
j = 0
h = 0
t = 1

while j < 10:
    while i < 100:
        random_number = random.randint(1, 2)
        if random_number == 1:
            # print("Heads")
            heads_count += 1
        else:
            # print("Tails")
            tails_count += 1
        i += 1

    print(f"{heads_count} {tails_count}")
    if heads_count > tails_count:
        h += 1
    else:
        t += 1
    heads_count = 0
    tails_count = 0
    i = 0
    j += 1

print(f"{h} {t}")
