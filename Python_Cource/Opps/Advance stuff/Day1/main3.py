# Ternary operations

a = 10
print("even") if a%2==0 else print("odd")

# List sets and dictionary Cpomprehension

# Normal form of list
l = []
for i in range(1,12):
    if i % 2 ==0:
        l.append(i)
print(l)

# List comprehension form

l = [i for i in range(1,21) if i%2 ==0] # First i hae to write the variable which i wnat to append that is i

print(l)


# Dictionary Comprehension form


l = {i : i**2 for i in range(1,21)}
print(l)
