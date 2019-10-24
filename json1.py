#json module:- javascript object notation
# it is a way to send data
import json
data = '{"var1":"ABCD", "var2":56}'
print(data)

parsed = json.loads(data)

print(parsed['var1'])
print(type(parsed))
data2={"Student_name":"ABCD",
        "Subjects":['Maths','computer','Python','English'],
        "Marks":[23,45,34,62],
}
jscomp= json.dumps(data2)  
print(jscomp) #now this is a javascript object
#jscomp is a javascript compatible object