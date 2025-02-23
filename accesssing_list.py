fruits=["Mango","Banana","apple"]
print("positon of fruits",fruits[2])
fruits.append("orrange")
print(fruits)
fruits.remove("Banana")
print(fruits)
fruits.pop(1)
print(fruits)

print("positon of fruits",fruits[-1])

squares = [x**2 for x in range(5)]
print(squares)