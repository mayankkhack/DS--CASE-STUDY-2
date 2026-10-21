 

users = ["A", "B", "C", "D"]

 
matrix = [[0 for j in users] for i in users]

# Friendship connections
friendships = [
    ("A", "B"),
    ("B", "C"),
    ("A", "D")
]

# Store friendship connections in the matrix
for person1, person2 in friendships:
    i = users.index(person1)
    j = users.index(person2)

    matrix[i][j] = 1
    matrix[j][i] = 1

# Display the adjacency matrix
print("Adjacency Matrix:")
print(" ", *users)

for i in range(len(users)):
    print(users[i], matrix[i])

# Check whether two users are friends
first = "A"
second = "B"

i = users.index(first)
j = users.index(second)

if matrix[i][j] == 1:
    print(first, "and", second, "are friends")
else:
    print(first, "and", second, "are not friends")
