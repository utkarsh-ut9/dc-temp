# Initialize the adjacency matrix for the distributed system
print('''
P1 P2 P3 P4 P5
P1 0 1 0 0 0
P2 0 0 1 0 0
P3 0 0 0 1 1
P4 1 0 0 0 0
P5 0 0 0 0 0
''')

# Initialize a list to hold the adjacency matrix
a = [
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

# Initialize a flag variable to indicate whether a deadlock was detected
flag = 0

# Define the function to detect deadlocks in the distributed system
def aman(a, i, k):
    end = 5
    for x in range(end):
        # Check if there is an edge from k to x
        if(a[k][x] == 1):
            # Check if x is the same as i (initiator site)
            if(i == x):
                print(f' S{k+1} ==> S{x+1} ({i+1}, {k+1}, {x+1}) --------> DEADLOCK DETECTED')
                global flag
                flag = 1
                break
            # Print the message indicating that a message was sent from k to x
            print(f' S{k+1} ==> S{x+1} ({i+1}, {k+1}, {x+1})')
            # Recursively call the function to continue the message-passing process
            aman(a,i,x)

# Print the header for the deadlock detection algorithm
print("CHANDY-MISRA-HAAS DISTRIBUTED DEADLOCK DETECTION ALGORITHM")
print("__________________________________________________________")
print()

# Ask the user to enter the initiator site number
x = 0
end = 5
i = int(input("Enter Initiator Site No. : "))
j = i - 1

print()

# Iterate over all the sites in the distributed system
for k in range(end):
    # Check if there is an edge from the initiator site to site k
    if(a[j][k]==1):
        # Print the message indicating that a message was sent from the initiator site to site k
        print(f' S{j+1} ==> s{k+1} ({i}, {j+1}, {k+1})')
        # Call the deadlock detection function for site k
        aman(a,j,k)

# If no deadlocks were detected, print a message indicating this
if(flag == 0):
    print("\nNO DEADLOCK DETECTED")

# Print the footer for the deadlock detection algorithm
print("__________________________________________________________")