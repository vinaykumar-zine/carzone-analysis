# import pandas as pd
# import numpy as np
# import random
# class Bank:
#     def __init__(self, Name, Age, AccNumber, AccType, Amount):
#         self.Name = Name
#         self.Age = Age
#         self.AccNumber = AccNumber
#         self.AccType = AccType
#         self.Amount = Amount
#     def open(self):
#         self.Name = input("Enter your Name:")
#         self.Age = input("Enter your Age:")
#         self.AccNumber = random.randint(100000000000,999999999999)
#         self.AccType = input("Enter your Account Type shaving or current:")
#         self.Amount = input("How much Amount you want to initially Credit:")
#     def deposite(self):
#         dep = float(input("Enter how much Amount you want to deposite:"))
#         self.Amount = self.Amount + dep
#         print(f"Your balance {dep}is successfully deposited and now your balance is {self.Amount}.")
#     def withdrow(self):
#         widrw = float(input("Enter how much Amount you want to withdrow:"))
#         if self.Amount>widrw:
#             self.Amount = self.Amount - wdrw
#             print(f"your balance {widrw} is duccessfully widrown and now your balance is {self.Amount}")
#         else:
#             print("Insufficient balance")
#     def details(self):
#         print(f"The {self.AccType} Account Holder Name is {self.Name} Whose Account number is {self.AccNumber},"
#                f" Now balance in His account is {self.Amount}.")
# acc = Bank(input("Enter Name:"), input("Age:"), random.randint(100000000000,999999999999), input("Acc type saving or current:"), input("How much you want to initially submit in bank:"))
import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
#
# data = pd.read_csv('district.csv')
# data.head()
#
# re=data.iloc[:30,5].values
# de=data.iloc[:30,4].values
# co=data.iloc[:30,3].values
# x=list(data.iloc[:30,0])
#
# plt.figure(figsize=(25,10))
# ax=plt.axes()
#
# ax.set_facecolor('black')
# ax.grid(linewidth=0.4, color='#8f8f8f')
#
#
# plt.xticks(rotation='vertical',
# 		size='20',
# 		color='white')#ticks of X
#
# plt.yticks(size='20',color='white')
#
#
# ax.set_xlabel('\nDistrict',size=25,
# 			color='#4bb4f2')
# ax.set_ylabel('No. of cases\n',size=25,
# 			color='#4bb4f2')
#
#
# plt.tick_params(size=20,color='white')
#
#
# ax.set_title('Maharashtra District wise breakdown\n',
# 			size=50,color='#28a9ff')
#
# plt.bar(x,co,label='re')
# plt.bar(x,re,label='re',color='green')
# plt.bar(x,de,label='re',color='red')
#
# for i,j in zip(x,co):
# 	ax.annotate(str(int(j)),
# 				xy=(i,j+3),
# 				color='white',
# 				size='15')
#
# plt.legend(['Confirmed','Recovered','Deceased'],
# 		fontsize=20)