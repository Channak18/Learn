# 1st way
# num = int(input("Enter your number"))
# if num < 0:
#     print("Negative number")
# else:
#     print("Positive number")

# 2nd way
# num = int(input("Enter your number"))
# result = "Positive number"
# if num < 0:
#     print("Negative number")
# else:
#     print("Positive number")

# ex2
# num = int(input("Enter number"))
# text = ""
# for i in range(num):
#     text = text + "x"
#     print(text)

# ex3
# num = int(input("Enter number"))
# for i in range(num, 1, -2):
#     for j in range(1, i + 1):
#         if j % 2 == 1:
#             print(j, end='')
#     print()

num = int(input("Your number"))
for i in range(num):
    if i % 2 != 0:
        for j in range(1, i + 1):
            if j % 2 != 0:
                 print(j, end="")
        print()