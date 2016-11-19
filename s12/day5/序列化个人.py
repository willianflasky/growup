import  pickle,json

f=open('user_acc.txt','r')

#data_from_atm =json.loads(f.read())
data_from_atm=json.load(f)

print(data_from_atm)