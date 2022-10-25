
# slice string
x = "so you yhink you can alone do oit for your own use but it cant be done by you. .."
y = "what did you gain by using this stuff , somebody will come for you, but it takaes time for yourself."
z = "chathoor vadekthil parijatham thripperumthura po chenithala"
print(x.upper())
print(z.upper())
print(x.lower())
print(z.lower())
print(y.lower())
print(y.upper())
print(type(x))
print(type(y))
print(type(z))
print(x.replace("e", "o"))
print(y.replace("r", "u"))
print(y.replace("k", "p"))
print(y.replace("h", "k"))
print(y.replace("l", "r"))
print(y.replace("y", "t"))
print(y.replace("a", "q"))
print(y.replace("t", "c"))
print(y.replace("d", "k"))
print(y.replace("k", "t"))
print(z.replace("chennithala", "chennai"))
print(x.split())
print(y.split())
print(z.split())
# mylist properties
mylist = [40, 20, 43, 56, 98, 89, 90, 87]
mylist[1:2] = [58, 300]
mylist[1:5] = [2000, 300]
mylist[0:4] = [200, 300]
mylist[0:6] = [200, 3000]
mylist[1:3] = [200, 300]
mylist[-6:2] = [200, 300]
mylist[1:-8] = [200, 300]
mylist[1:-6] = [200, 300]
mylist[-1:6] = [200, 300]
print(mylist)
mylist.clear()
print(mylist)
# arithmetic operator
print(100+10)
print(1056-20)
print(1090-20)
print(107*20)
print(106/20)
print(105//20)
print(105 % 20)
print(109**20)
