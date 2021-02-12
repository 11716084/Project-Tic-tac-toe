key_put = list('         ')

tic_toe = [key_put[numb:numb+3] for numb in range(0, len(key_put), 3)]

print(f"---------\n"
      f"| {tic_toe[0][0]} {tic_toe[0][1]} {tic_toe[0][2]} |\n"
      f"| {tic_toe[1][0]} {tic_toe[1][1]} {tic_toe[1][2]} |\n"
      f"| {tic_toe[2][0]} {tic_toe[2][1]} {tic_toe[2][2]} |\n"
      f"---------")

wrong_simbol = ['.', ',']
numeric_flag = False
l = 1
def checking2():
    if((tic_toe[0][0] != ' ') and tic_toe[0][0] == tic_toe[0][1] and tic_toe[0][1] == tic_toe[0][2]):
        print(tic_toe[0][0], "wins")
        exit()
    elif((tic_toe[1][0] != ' ') and tic_toe[1][0] == tic_toe[1][1] and tic_toe[1][1] == tic_toe[1][2]):
        print(tic_toe[1][2], "wins")
        exit()
    elif((tic_toe[2][0] != ' ') and tic_toe[2][0] == tic_toe[2][1] and tic_toe[2][1] == tic_toe[2][2]):
        print(tic_toe[2][0], "wins")
        exit()
    elif((tic_toe[0][0] != ' ') and tic_toe[0][0] == tic_toe[1][0] and tic_toe[1][0] == tic_toe[2][0]):
        print(tic_toe[0][0], "wins")
        exit()
    elif((tic_toe[0][1] != ' ') and tic_toe[0][1] == tic_toe[1][1] and tic_toe[1][1] == tic_toe[2][1]):
        print(tic_toe[0][1], "wins")
        exit()
    elif((tic_toe[0][2] != ' ') and tic_toe[0][2] == tic_toe[1][2] and tic_toe[1][2] == tic_toe[2][2]):
        print(tic_toe[0][2], "wins")
        exit()
    elif((tic_toe[0][0] != ' ') and tic_toe[0][0] == tic_toe[1][1] and tic_toe[1][1] == tic_toe[2][2]):
        print(tic_toe[0][0], "wins")
        exit()
    elif((tic_toe[2][0] != ' ') and tic_toe[2][0] == tic_toe[1][1] and tic_toe[1][1] == tic_toe[0][2]):
        print(tic_toe[2][0], "wins")
        exit()
    elif (tic_toe[0][0]!= " " and tic_toe[0][1]!= " " and tic_toe[0][2]!= " " and tic_toe[1][0]!= " " and tic_toe[1][1]!= " " and tic_toe[1][2]!= " " and tic_toe[2][0]!= " " and tic_toe[2][1]!= " " and tic_toe[2][2] != " "):
        print("Draw")
        exit()
def checking():
    global l
    while True:
        coordinates = input()

        for char in wrong_simbol:
            coordinates = coordinates.replace(char, ' ')

        coordinates = [int(coord) for coord in coordinates.split() if coord.isdigit()]

        if len(coordinates) != 2:
            print("You should enter numbers!")
            continue

        for coord in coordinates:
            if coord > 3 or coord < 1:
                numeric_flag = True
                break
            else:
                numeric_flag = False
        if numeric_flag:
            print("Coordinates should be from 1 to 3!")
            continue

        if tic_toe[coordinates[0]-1][coordinates[1]-1] == 'X' or tic_toe [coordinates[0]-1] [coordinates[1]-1] == 'O':
            print("This cell is occupied!")
            continue


        else:
            if l % 2 == 1:
                tic_toe[coordinates[0] - 1][coordinates[1] - 1] = 'X'
            if l % 2 == 0:
                tic_toe[coordinates[0] - 1][coordinates[1] - 1] = 'O'
            l += 1
        print(f"---------\n"
              f"| {tic_toe[0][0]} {tic_toe[0][1]} {tic_toe[0][2]} |\n"
              f"| {tic_toe[1][0]} {tic_toe[1][1]} {tic_toe[1][2]} |\n"
              f"| {tic_toe[2][0]} {tic_toe[2][1]} {tic_toe[2][2]} |\n"
              f"---------")
        checking2()
        checking()

checking()







# layout = [letter for letter in input("Enter cells:").replace('_', ' ')]
#
# def print_layout():
#     print('---------')
#     for i in range(0, 9, 3):
#         print(f"| {layout[i]} {layout[i + 1]} {layout[i + 2]} |")
#     print('---------')
#
# def process_input():
#     while True:
#         input_coordinate = input('Enter the coordinates:').split()
#         if input_coordinate[0].isnumeric() is False:
#             print("You should enter numbers!")
#         else:
#             x = int(input_coordinate[0])
#             y = int(input_coordinate[1])
#             if (1 <= x <= 3) and (1 <= y <= 3):
#                 if layout[(3 - y) * 3 + (x - 1)] == ' ':
#                     layout[(3 - y) * 3 + (x - 1)] = 'X'
#                     print_layout()
#                     break
#                 else:
#                     print('This cell is occupied! Choose another one!')
#             else:
#                 print('Coordinates should be from 1 to 3!')

# print_layout()
# process_input()





# seqs = [selection[:3], selection[3:6], selection[6:], selection[0] + selection[3] + selection[6],
#        selection[1] + selection[4] + selection[7], selection[2] + selection[5] + selection[8],
#        selection[0] + selection[4] + selection[8], selection[2] + selection[4] + selection[6]]
# count_X = [group.count("X") for group in seqs]
# count_O = [group.count("O") for group in seqs]
# if abs(selection.count("X") - selection.count("O")) > 1 or (3 in count_X and 3 in count_O):
#    print("Impossible")
# elif 3 in count_X:
#    print("X wins")
# elif 3 in count_O:
#    print("O wins")
# elif selection.count("_") == 0:
#    print("Draw")
# else:
#    print("Game not finished")

#_OOOO_X_X

# def checking():
#     while True:
#         global user_input
#         if user_input != int:
#             print("You should enter numbers!")
#             user_input = input("Enter the coordinates: ")
#         elif user_input != 1 or 2 or 3:
#             print("Coordinates should be from 1 to 3!")
#             user_input = input("Enter the coordinates: ")
#     print("good job")
# checking()






# num = int(input())
# for i in range(0, 1):
#     l=1
#     while l<=num*2:
#         print(("#"*l).center(num*2))
#         l+=2

    # print("")
# for i in range(0, int(input())):
#     print('#')

# string = "Pyt"
#
# new_string = string.center(24)
#
# print(new_string)


# X = input().split()
# list_reverse = X[::-1]
# print(" ".join(list_reverse))


# # List =[input()]
# X = "".join(input())
# list_reverse = X[::-1]
# print(list_reverse)

# x= input().split()
#
# print(" of ".join(x))

# text = input()
# text = text.replace("o", " ")
# text = text.split()
# text = " o".join(text)
# import math
# print("Enter cells:")
# x = input()
# print("---------")
# print("| "+ x[0] + " " + x[1] +" " + x[2] + " |")
# print("| "+ x[3] + " " + x[4] +" " + x[5] + " |")
# print("| "+ x[6] + " " + x[7] +" " + x[8] + " |")
# print("---------")
# def impossible():
#     Num = x.count('X') - x.count('O')
#     if abs(Num) >= 2:
#         print('Impossible')
#         exit()
# def impossible2():
#     l=0
#     if ((x[0] != '_', ' ') and x[0] == x[4] and x[4] == x[8]):    l+=1
#     if ((x[6] != '_', ' ') and x[6] == x[4] and x[4] == x[2]):    l+=1
#     if ((x[0] != '_', ' ') and x[0] == x[1] and x[1] == x[2]):    l+=1
#     if ((x[3] != '_', ' ') and x[3] == x[4] and x[4] == x[5]):    l+=1
#     if ((x[6] != '_', ' ') and x[6] == x[7] and x[7] == x[8]):    l+=1
#     if ((x[0] != '_', ' ') and x[0] == x[3] and x[3] == x[6]):    l+=1
#     if ((x[1] != '_', ' ') and x[1] == x[4] and x[4] == x[7]):    l+=1
#     if ((x[2] != '_', ' ') and x[2] == x[5] and x[8] == x[5]):    l+=1
#     if l >= 2:
#         print('Impossible')
#         exit()
#
#
#
# impossible()
# impossible2()
# # if x.count('_') > 0:
# #     print('Game not finished')
#
# if((x[0] != '_', ' ') and x[0] == x[4] and x[4] == x[8]):
#     print(x[0], "wins")
# elif((x[6] != '_', ' ') and x[6] == x[4] and x[4] == x[2]):
#     print(x[6], "wins")
# elif((x[0] != '_', ' ') and x[0] == x[1] and x[1] == x[2]):
#     print(x[0], "wins")
# elif((x[3] != '_', ' ') and x[3] == x[4] and x[4] == x[5]):
#     print(x[3], "wins")
# elif((x[6] != '_', ' ') and x[6] == x[7] and x[7] == x[8]):
#     print(x[6], "wins")
# elif((x[0] != '_', ' ') and x[0] == x[3] and x[3] == x[6]):
#     print(x[6], "wins")
# elif((x[1] != '_', ' ') and x[1] == x[4] and x[4] == x[7]):
#     print(x[7], "wins")
# elif((x[2] != '_', ' ') and x[2] == x[5] and x[8] == x[5]):
#     print(x[8], "wins")
# elif x.count('_') > 0:
#     print('Game not finished')
# else:
#     print('Draw')
# new_list sum(S[i, i+1]) for i in S]
# G  = [int(x) for x in input()]
# print([(G[x] = g[x=1]/2 for x in )])
# new_list  = input()
# S = [int(i) for i in new_list]
# G = []
# l=0
# for i in S:
#     G.append((sum(S[l: l+2]))/2)
#     l+=1
# (G.pop(-1))
# print(G)


# new_list = input()
# S = [int(i) for i in new_list]
# G = []
# l = 1
# for x in S:
#     G.append(sum(S[0:l]))
#     l += 1
# print(G)

#n = int(input())
#
# my_list = [1, 2]
# my_list2 = [my_list  for i in range(1) for i in range(n)]
# print(my_list2)
# str_1 = input()
# str_2 = input()
# str_3 = input()
# print(['str_', ['str_2'], [['str_3']]])

# print("Enter cells:")
# x = input()
# print("---------")
# print("| "+" "+ x[0] + " " + x[1] +" " + x[2] + " |")
# print("| "+" "+ x[3] + " " + x[4] +" " + x[5] + " |")
# print("| "+" "+ x[6] + " " + x[7] +" " + x[8] + " |")
# print("---------")

# numbers = [int(n) for n in input()]
#
# # change the next two lines
# less_than_5 = [x for x in numbers if x < 5]
# greater_than_5 = [x for x in numbers if x >5]
#
# # printing your results
# print(less_than_5)
# print(greater_than_5)


# number = range(1, 1000)
# g = [g for g in number if g % 3 == 0 ]
# print(g)

# new_list = input()
# S = [int(i) for i in new_list]
# G = []
# l = 1
# for x in S:
#     G.append(sum(S[0:l]))
#     l += 1
# print(G)




# # class Transaction:
# #     def __init__(self, number, funds, status="active"):
# #         self.number = number
# #         self.funds = funds
# #         self.status = status
# # payment = Transaction("000001", 9999.999)
# # print(payment)
#
# class Puppy:
#     n_puppies = 0  # number of created puppies
#
#     @property
#     def __new__(cls):
#         if cls.n_puppies < 10:
#             cls.n_puppies += 1
#             return object.__new__(cls)
#
#
# # define __new__
# class Test:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __repr__(self):
#         return "Test a:% s b:% s" % (self.a, self.b)
#
#     # Driver Code
#
#
# t = Test(1234, 5678)
# print(t)

# class Patient:
#     def __init__(self, name, last_name, age):
#         self.name = name
#         self.last_name = last_name
#         self.age = age
#
#     def __repr__(self):
#         return "Object of the class Patient. name: {}, last_name: {}, age: {}".format(self.name, self.last_name,
#                                                                                       self.age)
#
#     def __str__(self):
#         return "{} {}. {}".format(self.name, self.last_name, self.age)
#     # create methods here