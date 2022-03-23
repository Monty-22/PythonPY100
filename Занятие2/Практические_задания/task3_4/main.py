mount = 14
if 12 <= mount or mount <= 1:
    print("Что-то не то...")
if 3 <= mount <= 5:
    print("Весна")
elif mount in [5,6,7]:
    print("Лето")
elif mount in (9,10,11):
    print("Осень")
elif mount in {12,1,2} :
    print("Зима")
