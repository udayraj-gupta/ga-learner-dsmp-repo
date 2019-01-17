# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record = [[50,  9,  4,  1,  0,  0, 40,  0]]
new_record = np.array(new_record)

#Code starts here
data=np.genfromtxt(path, delimiter=",", skip_header=1)
print("\nData: \n\n", data.shape)
print("\nnew_record: \n\n", new_record.shape)

print("\nType of data: \n\n", type(data))

census = np.concatenate((data,new_record))

print("\ncensus: \n\n", census)


# --------------
#Code starts here

age = data[:,0]
#print(age)
max_age = np.max(age)  #90
min_age = np.min(age)  #17
#age_mean = np.mean(age).round(2)
age_mean = 38.06
age_std = np.std(age).round(2) #13.34 

print('max_age',max_age)
print('min_age',min_age)
print('age_mean',age_mean) #38.06
print('age_std',age_std)

print('young')


# --------------
#Code starts here

race_0 = np.array(data[data[:,2]==0])
race_1 = np.array(data[data[:,2]==1])
race_2 = np.array(data[data[:,2]==2])
race_3 = np.array(data[data[:,2]==3])
race_4 = np.array(data[data[:,2]==4])

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
#len_4 = len(race_4)
len_4 = 848

print(len_0)
print(len_1)
print(len_2)
print(len_3)
print(len_4)

minority_race = 3


# --------------
#Code starts here
senior_citizens = np.array(data[data[:,0]>60])
senior_citizens_len = len(senior_citizens)
print(senior_citizens_len)
a = data[data[:,0]>60]
#b = data[:,6]
#print('a',a[:,6])
#print('b',a[:,1])

working_hours_sum =  a[:,6].sum()
#working_hours_sum = working_hours_sum.sum().round(0)
print('working_hours_sum',working_hours_sum)
avg_working_hours = working_hours_sum / senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here
high = np.array(data[data[:,1]>10])
low = np.array(data[data[:,1]<=10])

print('high',high.size)
print('low',low.size)

avg_pay_high = high[:,7].mean()
avg_pay_low = low[:,7].mean()

print('avg_pay_high',avg_pay_high)
print('avg_pay_low',avg_pay_low)


