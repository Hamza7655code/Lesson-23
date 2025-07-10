Student_data = {
    'id1':{'name': 'sara','Grade': '5','Subject':'english, maths ,science'},
    'id2':{'name': 'mat','Grade': '7','Subject':'english, maths ,geogarphy'},
    'id3':{'name': 'sara','Grade': '5','Subject':'english, maths ,science'},
    'id4':{'name': 'tom','Grade': '10','Subject':'history, maths ,geogarphy'} 
}
result = {}
for key,value in Student_data.items():
    if value not in result.values():
        result[key] = value
print(result)