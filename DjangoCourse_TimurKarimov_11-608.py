while True:
    name = input("Enter file names ")
    name = name + ".html"
    try:
        file = open(name, 'w')
        break
    except FileNotFoundError:
        print("Invalid value ")
    except PermissionError:
        print("Invalid value ")
size = abs(int(float(input("Enter size of multiplication table "))))

matr = []
for i in range(size + 1): #Creating two-dimensional array
    matr.append([])
    for j in range(size + 1):
        matr[i].append(0)
for i in range(size + 1): #Fillin array
    for j in range(size + 1):
        if i == 0:
           matr[i][j] = j
        elif j == 0:
            matr[i][j] = i
        else:
            matr[j][i] = j*i

file.write("<HTML>\n<BODY>\nMultiplication table from 2 to " + str(size) + "\n" + "<TABLE>\n")
for j in range(size + 1):
    file.write("<tr>")  # Opening line
    for i in range(size + 1):
        result = str(matr[j][i])
        if j == i == 0:
            file.write("<td><b> " + "&nbsp" + "*" + "</b> </td>\n")
        elif i == j:
            file.write("<td><b> " + "&nbsp" + result + "</b> </td>\n")
            # Writes bold font of the squares of the numbers
        elif j == 0 or i == 0 and i != j:
            file.write("<td><u> " + "&nbsp" + result + "</u> </td>\n")
            # Writes underline font to the multiply numbers
        else:
            file.write("<td> " + "&nbsp" + result + " </td>\n")
            # Other table elements
    file.write("</tr>\n")  # Closing line
file.write("</TABLE>\n</BODY>\n</HEAD> ")
file.close()


