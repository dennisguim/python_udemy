s1 = set()
s1.add('dennis')
s1.add(1)
s1.update(('guim', 1, 2, 3, 4))
s1.discard('dennis')
s1.discard(1)

print(s1)

