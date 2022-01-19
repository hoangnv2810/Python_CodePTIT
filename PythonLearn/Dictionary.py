Dict = {}
print(type(Dict))
Dict[0] = 'Hoang'
Dict[2] = 'Nguyen'
Dict[3] = 1
print(Dict)
Dict['Value_set'] = 2, 3, 4
print(Dict)
Dict[0] = 'Hello'
print(Dict)
Dict[5] = {'Nested' :{'1': 'Life', '2' : 'Geeks'}}
print(Dict)
Dict = {'Dict1': {1: 'Geeks'},
        'Dict2': {'Name': 'For'}}
print(Dict['Dict1'])
print(Dict['Dict1'][1])
print(Dict['Dict2']['Name'])