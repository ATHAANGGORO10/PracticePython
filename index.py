nama = input("You System Operations :")
id = input("You Id Account :")
password = input("You Password :")

print(f"{nama, id, password}, Access Account")
print("If you delete it, it will damage your laptop")
print("It would be better to think about the impact")

tanggapan = input("Are You Sure You Want to Delete C:/Windows ? (Yes/No) ")

if tanggapan.lower() == "Yes":
    print("Congratulations, your operating system has been deleted")
elif tanggapan.lower() == "No":
    print("Operating System Removal Canceled")
else:
    print("Congratulations, your operating system has been deleted")