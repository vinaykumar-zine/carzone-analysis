import matplotlib.pyplot as plt
import matplotlib.pyplot as pp
import numpy as np
import pandas as pd
from gtts import gTTS
import os

dict = {
    "Name": ['Audi', 'Acura', 'BMW', 'Chevrolet', 'Ford', 'Honda', 'Hyundai', 'Isuzu', 'Jaguar', 'Jeep', 'Kia',
             'land Rove', 'Lincoln', 'Mazda', 'Mercedes', 'Nissan', 'Suzuki', 'Toyota', 'Volkswagen', 'Volvo'],

    "Price": ["45-50", "20-56", "22_23", "38_46", "19-22", "16-35", "15-25", "27-30", "22-30", "29-40", "19-30",
              "42-55", "30-38", "46-50", "21-38", "22-27", "15-25", "22-40", "17-22", "38-46"],
    "Mileage": ["17.42-20.12", "19.85-21.23", "17.65-20.22", "20.20-24.12", "13.25-17.56", "18.56-20.56", "16.58-20.56",
                "21.50-23.56", "19.60-20.36", "17.85-20.45", "22.12-24.52", "26.22-28.15", "23.50-24.53", "14.52-20.89",
                "17.46-18.25", "25.12-19.45", "23.41-25.36", "13.69-15.21", "20.25-21.65", "22.63-25.13"],
    "EnzineSize":[3.5,2,2.25,3.5,3,2.7,3.0,2.5,2.27,3.4,4.2,3.5,3.02,2.5,2.88,2.87,4.5,4,3.7,2.08],
    "Weight":[4550,2056,3223,3836,3092,3665,2525,2755,2287,3294,4190,2955,3002,4160,4218,3227,4155,41240,31702,2386],
"Availability":["Asia and America","Asia and America","Europe,Asia and America","Asia,Europe and America","Asia ,Europe and America","Antartica,Asia and America","Asia and America","Europe and America","Asia and America","Asia and America","Asia and America","Asia and America","Asia,Europe and America","Europe,Asia and America","Asia,Antartica and America","Asia,Antartica and America","Asia and America","Asia and America","Europe and America","Asia and America"]

}

Car=pd.DataFrame(dict)
print(Car)

# **Car sales Analysis**

txt = "Enter one for Audi, Two for Acura, Three for BMW, Four for Chevrolet, five for Ford, six for Honda, seven for Hyundai, Eight for Isuzu, Nine for Jaguar, ten for Jeep, Eleven for Kia, Twelve for land Rove, Thirteen for Lincoln, fourteen for Mazda, fifteen for Mercedes, sixteen for Nissan, seventeen for Suzuki, Eighteen for Toyota,Nineteen for Volkswagen, Twenty for Volvo "
language = 'en'

myobj = gTTS(text=txt, lang=language, slow=False)

myobj.save("txt.mp3")

os.system("start txt.mp3")
print('Enter your car number:\n')

X, Y = [], []
c =int(input('enter car no.'))
if c==1:
    for line in open('audi.txt', 'r'):
        values = [float(s) for s in line.split()]
        X.append(values[0])
        Y.append(values[1])


    plt.plot(X, Y)
    plt.title("Audi sales stat")
    plt.ylabel("no. of cars")
    plt.xlabel("year")
    plt.show()
elif c==2:
     for line in open('Acura.txt', 'r'):
       values = [float(s) for s in line.split()]
       X.append(values[0])
       Y.append(values[1])

     plt.plot(X, Y)
     plt.title("Acura sales stat")
     plt.ylabel("no. of cars")
     plt.xlabel("year")
     plt.show()
elif c==3:
     for line in open('bmw.txt', 'r'):
       values = [float(s) for s in line.split()]
       X.append(values[0])
       Y.append(values[1])

     plt.plot(X, Y)
     plt.title("BMW sales stat")
     plt.ylabel("no. of cars")
     plt.xlabel("year")
     plt.show()
elif c==4:
    for line in open('Chevrolet.txt', 'r'):
        values = [float(s) for s in line.split()]
        X.append(values[0])
        Y.append(values[1])

    plt.plot(X, Y)
    plt.title("Chevrolet sales stat.")
    plt.ylabel("no. of cars")
    plt.xlabel("year")
    plt.show()
elif c==5:
    for line in open('Ford.txt', 'r'):
        values = [float(s) for s in line.split()]
        X.append(values[0])
        Y.append(values[1])

    plt.plot(X, Y)
    plt.title("Ford sales stat.")
    plt.ylabel("no. of cars")
    plt.xlabel("year")
    plt.show()
elif c==6:
    for line in open('Honda.txt', 'r'):
      values = [float(s) for s in line.split()]
      X.append(values[0])
      Y.append(values[1])

    plt.plot(X, Y)
    plt.title("Honda sales stat.")
    plt.ylabel("no. of cars")
    plt.xlabel("year")
    plt.show()
elif c==7:
    for line in open('Hyundai.txt', 'r'):
      values = [float(s) for s in line.split()]
      X.append(values[0])
      Y.append(values[1])

    plt.plot(X, Y)
    plt.title("Hyundai sales stat.")
    plt.ylabel("no. of cars")
    plt.xlabel("year")
    plt.show()
elif c==8:
    for line in open('Isuzu.txt', 'r'):
        values = [float(s) for s in line.split()]
        X.append(values[0])
        Y.append(values[1])

    plt.plot(X, Y)
    plt.title("Isuzu sales stat.")
    plt.ylabel("no. of cars")
    plt.xlabel("year")
    plt.show()
elif c==9:
    for line in open('Jaguar.txt', 'r'):
        values = [float(s) for s in line.split()]
        X.append(values[0])
        Y.append(values[1])

    plt.plot(X, Y)
    plt.title("Jaguar sales stat.")
    plt.ylabel("no. of cars")
    plt.xlabel("year")
    plt.show()
elif c==10:
    for line in open('Jeep.txt', 'r'):
        values = [float(s) for s in line.split()]
        X.append(values[0])
        Y.append(values[1])

    plt.plot(X, Y)
    plt.title("Jeep sales stat.")
    plt.ylabel("no. of cars")
    plt.xlabel("year")
    plt.show()
elif c==11:
    for line in open('Kia.txt', 'r'):
        values = [float(s) for s in line.split()]
        X.append(values[0])
        Y.append(values[1])

    plt.plot(X, Y)
    plt.title("Kia sales stat.")
    plt.ylabel("no. of cars")
    plt.xlabel("year")
    plt.show()
elif c==12:
    for line in open('landRove.txt', 'r'):
       values = [float(s) for s in line.split()]
       X.append(values[0])
       Y.append(values[1])

    plt.plot(X, Y)
    plt.title("land Rove sales stat.")
    plt.ylabel("no. of cars")
    plt.xlabel("year")
    plt.show()
elif c==13:
    for line in open('Lincoln.txt', 'r'):
        values = [float(s) for s in line.split()]
        X.append(values[0])
        Y.append(values[1])

    plt.plot(X, Y)
    plt.title("Lincoln sales stat.")
    plt.ylabel("no. of cars")
    plt.xlabel("year")
    plt.show()
elif c==14:
    for line in open('Mazda.txt', 'r'):
        values = [float(s) for s in line.split()]
        X.append(values[0])
        Y.append(values[1])

    plt.plot(X, Y)
    plt.title("Mazda sales stat.")
    plt.ylabel("no. of cars")
    plt.xlabel("year")
    plt.show()
elif c==15:
    for line in open('Mercedes.txt', 'r'):
        values = [float(s) for s in line.split()]
        X.append(values[0])
        Y.append(values[1])

    plt.plot(X, Y)
    plt.title("Mercedes sales stat.")
    plt.ylabel("no. of cars")
    plt.xlabel("year")
    plt.show()
elif c==16:
    for line in open('Nissan.txt', 'r'):
        values = [float(s) for s in line.split()]
        X.append(values[0])
        Y.append(values[1])

    plt.plot(X, Y)
    plt.title("Nissan sales stat.")
    plt.ylabel("no. of cars")
    plt.xlabel("year")
    plt.show()
elif c==17:
    for line in open('Suzuki.txt', 'r'):
        values = [float(s) for s in line.split()]
        X.append(values[0])
        Y.append(values[1])

    plt.plot(X, Y)
    plt.title("Suzuki sales stat.")
    plt.ylabel("no. of cars")
    plt.xlabel("year")
    plt.show()
elif c==18:
    for line in open('Toyota.txt', 'r'):
        values = [float(s) for s in line.split()]
        X.append(values[0])
        Y.append(values[1])

    plt.plot(X, Y)
    plt.title("Toyota sales stat.")
    plt.ylabel("no. of cars")
    plt.xlabel("year")
    plt.show()
elif c==19:
    for line in open('Volswagen.txt', 'r'):
        values = [float(s) for s in line.split()]
        X.append(values[0])
        Y.append(values[1])

    plt.plot(X, Y)
    plt.title("Volkswagen sales stat.")
    plt.ylabel("no. of cars")
    plt.xlabel("year")
    plt.show()
elif c==20:
    for line in open('Volvo.txt', 'r'):
        values = [float(s) for s in line.split()]
        X.append(values[0])
        Y.append(values[1])

    plt.plot(X, Y)
    plt.title("Volvo sales stat.")
    plt.ylabel("no. of cars")
    plt.xlabel("year")
    plt.show()

print("These are models of car choosing by you.....")
print('1. Santa')
print('2. Accent')
print('3. Elantra')
print('4. Sonata')

print('-----Comparision------')

mytext = "For comparison in models. Enter one for Engine, Two for Price, Three for Airbags, four for Mileage and five for Capacity."
language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("output.mp3")

os.system("start output.mp3")
print("Enter 1 for Engine, 2 for Price, 3 for Airbags, 4 for Mileage and 5 for Capacity.")


b = int(input("Enter your choice  for comparison:"))

if b == 1:
    text1 = "You have pressed key one, So this graph given here shows the comparison of engines in your selected car in model."
    language = 'en'

    myobj = gTTS(text=text1, lang=language, slow=False)

    myobj.save("Engine.mp3")

    os.system("start Engine.mp3")
    data = np.loadtxt(fname='engine.csv', delimiter=',')
    a = ['red', 'blue', 'green', 'orange']

    X = []
    Y = []

    for i in range(len(data)):
        for j in range(2):
            if j == 0:
                X.append(data[i][j])
            else:
                Y.append(data[i][j])

    pp.bar(X, Y, width=0.6, color=a)
    pp.xlabel('Serial Number of Model')
    pp.ylabel('Price in hp')
    pp.title('Engine Comparision')
    pp.show()
elif (b == 2):
    text2 = "You have pressed key Two, So this graph given here shows the comparison of Price in your selected car in model."
    language = 'en'

    myobj = gTTS(text=text2, lang=language, slow=False)

    myobj.save("Price.mp3")

    os.system("start Price.mp3")
    data = np.loadtxt(fname='price.csv', delimiter=',')

    X = []
    Y = []

    for i in range(len(data)):
        for j in range(2):
            if j == 0:
                X.append(data[i][j])
            else:
                Y.append(data[i][j])

    a = ['red', 'blue', 'green', 'orange']

    pp.bar(X, Y, width=0.6, color=a)
    pp.xlabel('Serial Number of Model')
    pp.ylabel('Price in lakh')
    pp.title('Comparision of Price')
    pp.show()
elif (b == 3):
    text3 = "You have pressed key Three, So this graph given here shows the comparison of Airbags in your selected car in model."
    language = 'en'

    myobj = gTTS(text=text3, lang=language, slow=False)

    myobj.save("Airbags.mp3")

    os.system("start Airbags.mp3")
    data = np.loadtxt(fname='airbags.csv', delimiter=',')

    X = []
    Y = []

    for i in range(len(data)):
        for j in range(2):
            if j == 0:
                X.append(data[i][j])
            else:
                Y.append(data[i][j])

    a = ['red', 'blue', 'green', 'orange']

    pp.bar(X, Y, width=0.6, color=a)
    pp.xlabel('Serial Number of Model')

    pp.title('Airbags Comparision')
    pp.show()

elif (b == 4):
    text4 = "You have pressed key four, So this graph given here shows the comparison of Mileage in your selected car in model."
    language = 'en'

    myobj = gTTS(text=text4, lang=language, slow=False)

    myobj.save("Mileage.mp3")

    os.system("start Mileage.mp3")
    data = np.loadtxt(fname='Mileage.csv', delimiter=',')

    X = []
    Y = []

    for i in range(len(data)):
        for j in range(2):
            if j == 0:
                X.append(data[i][j])
            else:
                Y.append(data[i][j])

    a = ['red', 'blue', 'green', 'orange']

    pp.bar(X, Y, width=0.6, color=a)
    pp.xlabel('Serial Number of Model')
    pp.ylabel('Price in KM')
    pp.title('Milage Comparision')
    pp.show()
elif (b == 5):
    text5 = "You have pressed key five, So this graph given here shows the comparison of Capacity in your selected car in model."
    language = 'en'

    myobj = gTTS(text=text5, lang=language, slow=False)

    myobj.save("Capacity.mp3")

    os.system("start Capacity.mp3")
    data = np.loadtxt(fname='capacity.csv', delimiter=',')

    X = []
    Y = []

    for i in range(len(data)):
        for j in range(2):
            if j == 0:
                X.append(data[i][j])
            else:
                Y.append(data[i][j])

    a = ['red', 'blue', 'green', 'orange']

    pp.bar(X, Y, width=0.6, color=a)
    pp.xlabel('Serial Number of Model')
    pp.ylabel('NUMEBER OF MEMBERS')
    pp.title('Capacity Comparision')
    pp.show()
else:
    text6 ="You Entered wrong input. Please give right input from given as one for Engine, Two for Price, Three for Airbags, four for Mileage and five for Capacity."

    language = 'en'

    myobj = gTTS(text=text6, lang=language, slow=False)

    myobj.save("elsee.mp3")

    os.system("start elsee.mp3")
    print("You Entered wrong input. Please give right input from given as 1 for Engine, 2 for Price, 3 for Airbags, 4 for Mileage and 5 for Capacity.")
    print("Run for again..........")