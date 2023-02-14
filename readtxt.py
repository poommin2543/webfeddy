# f = open("nameid.txt", "r")
# # print(f.read())
# fp = f.read()
#an empty dictionary
 
dictionary = {}
with open("nameid.txt") as file:
 for line in file:
    (key, value) = line.split(":")
    value = (value.split("\n"))[0]
    dictionary[int(key)] = value
label = dictionary[0]
print(label)