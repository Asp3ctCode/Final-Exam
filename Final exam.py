#Tyler Goodrich
#3/13/19
#This program will take your budget and it will give you the specs of what pc you should build.

budget = int(input("Hello lets get started what is your budget?:"))
print("  ")
games = input("List 3 of your favorite PC games:")
print("    ")
for x in games:
    print("Perfect Budget and Great Choice of games.")
    print("   ")

    if budget >= 450 and budget < 500:
        print("These are you specs, Processer: Intel i3  GPU: Gtx 980  Ram: 4gb ballistix ddr4 Case: Thermaltake CA-1B3-00M1NN-00 Versa")
        print("   ")
budget = int(input("What is your budget?"))

    elif budget >= 550 and budget < 600:
        print("These are your specs, Processer: Intel i5 7700 GPU: Gtx 980  Ram: 4gb ballistix ddr4 Case: ")
        
        break
    else:
        print('That is not a real Budget')
