import pandas as pd
import os
import random

df = pd.read_csv("../csv_files/onecompletejourney/adam.csv")

numOfCsv = int(input("enter the number of csvs you need ?"))
name_of_folder = input("enter the folder name: ")

noice = int(input('''

Enter the noice that you want
1. low
2. medium
3. Burn the dataset
4. let god be a witness to my sins

'''))

def calculate_avg_speed(avg_speed, newAvg_Speed):
    #this method called when we need to find avg of past 5 hours of speed data
    for item in avg_speed:
        summ = 0.0
        if avg_speed.index(item)<5:
            for i in range(avg_speed.index(item)):
                summ += avg_speed[i]

            if avg_speed.index(item) == 0:

                newAvg_Speed.append(item)
            else:
                newSum = summ/avg_speed.index(item)

                newAvg_Speed.append(newSum)
        else:
            for i in range(avg_speed.index(item)-5, avg_speed.index(item)):
                summ += avg_speed[i]

            newSum = summ/5

            newAvg_Speed.append(newSum)
    return newAvg_Speed

def signs():
    return random.choice([-1, 1])
def speedSelect():
    return random.uniform(0.01, 0.9)

def speedSelect():
    return random.uniform(0.05, 0.1)

def newTimestamp(date1):
    dateFormat = '%Y-%m-%dT%H:%M:%S'
    date2 = date1[:-7]+str(random.randint(10,100))
    return date2+date1[-5:]

def normalise(d1, d2):
    if d1==-1:

        return np.nan
    else:

        return d1/d2
def randomVal(choice, choice2 ):
    selectChoice = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    if choice == 1:
        if selectChoice > 3 and selectChoice <= 10:
            #print("++")
            if choice2 == 1:
                return 1
            else:
                return 1
        elif selectChoice == 1:
            #print("-+")
            if choice2 == 1:
                return -1
            else:
                return 1
        elif selectChoice== 2:
            #print("+-")
            if choice2 == 1:
                return 1
            else:
                return -1
        else:
            #print("--")
            if choice2 == 1:
                return -1
            else:
                return -1
    elif choice == 2:
        if selectChoice > 3 and selectChoice <= 10:
            #print("-+")
            if choice2 == 1:
                return -1
            else:
                return 1
        elif selectChoice == 1:
            #print("++")
            if choice2 == 1:
                return 1
            else:
                return 1
        elif selectChoice== 2:
            #print("+-")
            if choice2 == 1:
                return 1
            else:
                return -1
        else:
            #print("--")
            if choice2 == 1:
                return -1
            else:
                return -1
    elif choice == 3:
        if selectChoice > 3 and selectChoice <= 10:
            #print("+-")
            if choice2 == 1:
                return 1
            else:
                return -1
        elif selectChoice == 1:
            #print("-+")
            if choice2 == 1:
                return -1
            else:
                return 1
        elif selectChoice== 2:
            #print("++")
            if choice2 == 1:
                return 1
            else:
                return 1
        else:
            if choice2 == 1:
                return -1
            else:
                return -1
            #print("--")

    else:
        if selectChoice > 3 and selectChoice <= 10:
            #print("--")
            if choice2 == 1:
                return -1
            else:
                return -1
        elif selectChoice == 1:
            #print("-+")
            if choice2 == 1:
                return -1
            else:
                return 1
        elif selectChoice== 2:
            #print("+-")
            if choice2 == 1:
                return 1
            else:
                return -1
        else:
            #print("++")
            if choice2 == 1:
                return 1
            else:
                return 1
'''
for really stable dataset (one that matches very close to the adam.csv) use 0.005 to 0.01
for a little distorted dataset use 0.01 to 0.009
for really messed up dataset use 0.01 to 0.09
if you feel like i need to reboot use 0.1 to 0.9
'''
noice_data= []
if noice == 1:
    noice_data.append(0.005)
    noice_data.append(0.01)
elif noice==2:
    noice_data.append(0.01)
    noice_data.append(0.009)
elif noice == 3:
    noice_data.append(0.01)
    noice_data.append(0.09)
else:
    noice_data.append(0.1)
    noice_data.append(0.9)

os.mkdir(path="../generated_csvs/"+name_of_folder)
for index in range(numOfCsv):
    newDf = pd.DataFrame(df, columns=['Timestamp', 'Latitude', 'Longitude','Size_A', 'Size_B', 'Size_C', 'Size_D', 'Width', 'Length', 'SOG', 'COG', 'ROT', 'ETA-Hours', 'ata-hour', 'distance_travelled'])
    choice = random.choice([1,2,3,4])
    '''
    1-> high priority is give to + lat,+ lon
    2-> to -, +
    3-> to +,-
    4-> to -,-

    choice2 -> 1 or 2
    1-> lat
    2-> lon
    '''

    '''
    choice2 -> 1 or 2
    1-> lat
    2-> lon
    '''

    newDf['Timestamp'] = newDf['Timestamp'].apply(lambda row: newTimestamp(row))

    newDf['Latitude'] = newDf['Latitude'].apply(lambda row: float(row) + randomVal(choice, 1)*(random.uniform(noice_data[0], noice_data[1])))
    newDf['Longitude'] = newDf['Longitude'].apply(lambda row: float(row) + randomVal(choice, 2)*(random.uniform(noice_data[0], noice_data[1])))

    newDf['SOG'] = newDf['SOG'].apply(lambda row: row + signs()*speedSelect())

    newETA = (df['ETA-Hours'][0]*newDf['SOG'].mean())/df['SOG'].mean()
    newDf['ETA-Hours']= newETA

    avg_speed = list(newDf['SOG'])
    newAvg_Speed = []
    #avg_sog is the average of speed from past 5 hours
    newDf['avg_sog']=calculate_avg_speed(avg_speed, newAvg_Speed)

    newDf['COG'] = newDf['COG'].apply(lambda row: row + signs()*speedSelect())

    maximo = newDf['distance_travelled'].max()
    newDf['journey_completed'] = newDf['distance_travelled'].apply(lambda row: round(normalise(row, maximo)*100, 2))
    newDf['journey_completed']

    #ata must always be in the last
    newAta = (df['ata-hour'][0]*newDf['SOG'].mean())/df['SOG'].mean()
    newDf['ata-hour'] = newAta

    path = "../generated_csvs/"+name_of_folder+"/"+str(index)+".csv"
    newDf.to_csv(path)
print("it is done!!!")
