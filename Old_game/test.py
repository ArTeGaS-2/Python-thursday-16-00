#Інгредієнти піци:
#Томат
#Тісто
#Ковбаса
#Сир

#Ingredients

#Чи є у списку компонент з назвою "Чілі"

list_of_ingredients = ["Томат","Тісто", "Ковбаса", "Сир"]
title = "Інгредієнти піци:"
print(title)
for ingredient in list_of_ingredients:
    print(ingredient)

if "Чілі" in list_of_ingredients:
    print("Чілі присутнє")
else:
    print("Чілі відсутнє")