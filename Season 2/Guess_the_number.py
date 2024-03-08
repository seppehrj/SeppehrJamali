import random

pc_number = random.randint(1, 100)
print("Adad Beyn (1 ta 100) ast va shoma 15 forsat baray Hads Dorost Adad Darid")
print("Good Lock")
x = int()
while True:
    human_number = int(input("Hads bezan: "))
   

    if pc_number == human_number:
        x = x + 1
        print("Nice Shoma Barande Shodid")
        print("✔")
        print("Tedad Hads: ", x)
        break
        

    elif pc_number > human_number:
        x = x + 1
        print("Adad Nadorost Ast")
        print("Rahnamayi: Adad Mored nazar Bala Tar ⏫ az hads Shomast")
        print("❌")
    elif pc_number < human_number:
        x = x + 1
        print("Adad Nadorost Ast")
        print("Rahnamayi: Adad Mored nazar Payin Tar ⏬ az hads Shomast")
        print("❌")