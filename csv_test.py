with open("PhillipsParkZooCollection.csv", 'r') as f:
    doc = f.read()

doc_lines = doc.split(',\n')
queries: str = []
for line in doc_lines:
    tmp = line.split(',')
    for t in tmp:
        if t != '':
            queries.append(t)
print(queries)