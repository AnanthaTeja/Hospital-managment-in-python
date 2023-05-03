s=input()
with open(r'Doctors_DataBase.csv', 'r') as fp:
    lines = fp.readlines()
    for line in lines:
        if line.find(s) != -1:
            print(s, 'string exists in file')
            print('Line Number:', lines.index(line))
            print('Line:', line)
    else:
        print("not preesent")
