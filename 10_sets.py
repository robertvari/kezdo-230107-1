A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

#print(B)
# union
#print(A | B)

# difference
#print(A - B)
#print(B - A)

# intersection
#print(A & B)

# symmetrical difference
#print(A ^ B)

# add item to set
#A.add(20)
#print(A)

# add multiple items
#A.update([100, 200, 300])
#print(A)

print(A|B - A&B)
print((A|B) - (A&B))