relatives = []
noOfRelatives = int(input("Enter No. of relatives: "))
for i in range(0, noOfRelatives):
      relatives.append(input("Enter Name of {} Relative: ".format(i+1)))
sum = 0
for i in range(0, len(relatives)):
      a = int(input("Enter the Eidi of "+relatives[i]+": "))
      sum = sum+a
print("Total Eidi: ",sum)