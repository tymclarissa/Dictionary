dict = {"flowers":" Clarissa",55: "Fail" , "key2":1234}
print(dict["flowers"])
print(dict[55])
print(dict["key2"])
dict["candy"] = "lolipop"
print(dict["candy"])
print(dict)
del dict["key2"]
print(dict)
dict["candy"] = "chocolate"

for key in dict.keys():
    print(key , "->", dict[key])


