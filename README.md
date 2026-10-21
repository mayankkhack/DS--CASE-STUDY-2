Case Study 2: Social Network Friendship Connections Using an Adjacency Matrix

Unit II: Searching and Sorting / Arrays

Subject: Data Structures and Algorithms (DSA)
Programming Language: Python 3

Aim

To represent users and their friendship connections using an adjacency matrix.

Objectives

* Represent users as vertices in a graph.
* Store friendship connections using a matrix.
* Check whether two users are directly connected.
* Understand the use of graphs in social networking applications.

Theory

An adjacency matrix is a two-dimensional array used to represent connections between vertices in a graph.

* 1 indicates a connection between two users.
* 0 indicates no direct connection.
* In an undirected friendship graph, the matrix is symmetric.

Algorithm

1. Create a list of users.
2. Initialize a square matrix with zeroes.
3. Mark friendship connections as 1 in both corresponding positions.
4. Check the matrix entry for the two users.
5. Display the matrix and friendship result.

Sample Input

Users: ["A", "B", "C", "D"]

Friendships: A–B, B–C, A–D

Sample Output

   A B C D
A [0, 1, 0, 1]
B [1, 0, 1, 0]
C [0, 1, 0, 0]
D [1, 0, 0, 0]
A and B are friends

Complexity

* Matrix initialization: O(V²)
* Friendship check: O(1) after locating the users’ indices.
* Space complexity: O(V²)

Applications

* Social networking applications.
* Checking direct user connections.
* Representing undirected graphs.

How to Run

Run the Python program using:

python main.py

Conclusion

An adjacency matrix represents social network connections and allows direct friendship checks in constant time after the users’ indices are known.

Case Study 2 — Unit II
