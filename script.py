print("beta version")

# equation 1
x1 = float(input("enter x1 : "))
y1 = float(input("enter y1 : "))
z1 = float(input("enter z1 : "))
c1 = float(input("enter c1 : "))

# equation 2
x2 = float(input("enter x2 : "))
y2 = float(input("enter y2 : "))
z2 = float(input("enter z2 : "))
c2 = float(input("enter c2 : "))

# equation 3
x3 = float(input("enter x3 : "))
y3 = float(input("enter y3 : "))
z3 = float(input("enter z3 : "))
c3 = float(input("enter c3 : "))

# number of iterations
number_of_iterations = int(input("enter number of iterations: "))

# starting values
aux_x1 = 0.0
aux_x2 = 0.0
aux_x3 = 0.0

for k in range(0, number_of_iterations):
    # calculating x1
    new_x = ((c1)-(y1*(aux_x2))-(z1*aux_x3))/x1
    new_y = ((c2)-(x2*(aux_x2))-(z2*aux_x3))/y2
    new_z = ((c3)-(x3*(aux_x2))-(y3*aux_x3))/z3

    print("iteration number: ", k+1)
    print("value of x(" + str((k+1)) + ") :", new_x)
    print("value of y(" + str((k+1)) + ") :", new_y)
    print("value of z(" + str((k+1)) + ") :", new_z)

    aux_x1 = new_x
    aux_x2 = new_y
    aux_x3 = new_z