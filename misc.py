with open('classes.csv', 'r') as f:
    classes_str = f.read()

queries = classes_str.split(',')

no_repeats =[]

r_count = 0

for q in queries:
    if q not in no_repeats:
        no_repeats.append(q)
    else:
        print("repeat found,  discarding")
        r_count += 1
    print("Found " + str(r_count) + " repeats\n")

    with open('classes.csv', 'w') as f:
        f.write(no_repeats)
