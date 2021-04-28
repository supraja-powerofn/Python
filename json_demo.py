import json

#Converting json to dict
json_obj = '''{
    "id" : 1,
    "name" : "ABC",
    "Location" : { " lat" : 23.79, "lon" : 43.65} 
}'''

parsed_obj = json.loads(json_obj)

print(parsed_obj)
print(parsed_obj["name"])

#Converting dict to json
dict_obj = {
    "name" : "A",
    "group" : 2 
}
json_conv = json.dumps(dict_obj,indent = 4,sort_keys = True)  #JSON obj
print(json_conv)

print(json.dumps([1,2,3,4]))            #Array
print( json.dumps(("A",1,"B",2)) )      #Array
print( json.dumps("A string here") )    #String
print( json.dumps(3.14) )               #Number
print( json.dumps(True) )               #true
print( json.dumps(None) )               #null

