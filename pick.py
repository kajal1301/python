#pickle module
import pickle
#pickling a python object
cars= ["Maruti","Hyundai","Audi"]
file= "mycar.pkl"
fileobj= open(file,'wb')
pickle.dump(cars, fileobj)
fileobj.close

#depickling a file object
file= "mycar.pkl"
fileobj= open(file,'rb')
mycar= pickle.load(fileobj)
print(mycar)
print(type(mycar))
#pickle is considered as a security threat