
a = int(input("your Marks in Autocad:"));
X = " "
if (a >= 80 and a <= 100):
    X = 'A-One'
elif (a >= 70 and a < 80):
    X = 'A'
elif (a >= 60 and a < 70):
    X = 'B'
elif (a >= 50 and a < 60):
    X = 'C'
elif (a >= 40 and a < 50):
    X = 'D'
elif (a >= 33 and a < 40):
    X = 'E'
elif (a >= 0 and a < 33):
    X = 'FAIL'
else:
    X = "inappropriate score"
#-----------------------------------------------------------#        
b = int(input("your Marks in Proe:"));
Y = " "
if (b >= 80 and b <= 100):
    Y = 'A-One'
elif (b >= 70 and b < 80):
    Y = 'A'
elif (b >= 60 and b < 70):
    Y = 'B'
elif (b >= 50 and b < 60):
    Y = 'C' 
elif (b >= 40 and b < 50):
    Y = 'D'
elif (b >= 33 and b < 40):
    Y = 'E'
elif (b >= 0 and b < 33):
    Y = 'FAIL'
else:
    Y = "inappropriate score"

#-------------------------------------------------------------#
c = int(input("your Marks in C-Language:"));
Z = " " 
if (c >= 80 and c <= 100):
    Z = 'A-One'
elif (c >= 70 and c < 80):
    Z = 'A'
elif (c >= 60 and c < 70):
    Z = 'B'
elif (c >= 50 and c < 60):
    Z = 'C'
elif (c >= 40 and c < 50):
    Z = 'D'
elif (c >= 33 and c < 40):
    Z = 'E' 
elif (c >= 0 and c < 33):
    Z = 'FAIL'
else:
    Z = "inappropriate score"
#-------------------------------------------------------------#


d = int(input("your Marks in Photoshop:"));
v = " "
if (d >= 80 and d <= 100):
    v = 'A-One'
elif (d >= 70 and d < 80):
    v = 'A'
elif (d >= 60 and d < 70):
    v = 'B'
elif (d >= 50 and d < 60):
    v = 'C'
elif (d >= 40 and d < 50):
    v = 'D'
elif (d >= 33 and d < 40):
    v = 'E'
elif (d >= 0 and d < 33):
    v = 'FAIL'
else:
    v = "inappropriate score"
#-----------------------------------------------------------#


e = int(input("your Marks in Premier Pro:"));
w = " "
if (e >= 80 and e <= 100):
    w = 'A-One'
elif (e >= 70 and e < 80):
    w = 'A'
elif (e >= 60 and e < 70):
    w = 'B'
elif (e >= 50 and e < 60):
    w = 'C'
elif (e >= 40 and e < 50):
    w = 'D'
elif (e >= 33 and e < 40):
    w = 'E'
elif (e >= 0 and e < 33):
    w = 'FAIL'
else:
    w = "inappropriate score"
#-----------------------------------------------------------#
print("Gnenrating your Marksheet..........................................")

print('\n' + "Subject  Marks Grade" '\n')
print('\n' + "Autocad" + " " + str(a) + " " + str(X) )
print('\n' + "Proe" + " " + str(b) + " "+str(Y) )
print('\n' + "C-Language" + " " + str(c) + " " + str(Z) )
print('\n' + "Photoshop" + " " + str(d) + " " + str(v) )
print('\n' + "Premier Pro" + " " + str(e) + " " + str(w) )
total = a + b + c + d + e
print('\n' + "your Total Marks are:" + " " + str(total))
