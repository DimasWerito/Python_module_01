"""
Повернімося до завдання з пункту 8 для розрахунку площі.
 Ширина та висота задані у рядковому вигляді.
 Необхідно, як і раніше, розрахувати площу, 
 але потрібно рядковий тип перетворити на чисельний (float) при розрахунку площі area. 
 Не забудьте також додати до змінної show рядок з наступним шаблоном:
 'With width <значення ширини> and length <значення довжини> of the room, its area is equal to <значення площі>'.
"""


length = "2.75"
width = "1.75"
area = float(length) * float(width)
show = f"With width {float(width)} and length {float(length)} of the room, its area is equal to {area}"
print(show)