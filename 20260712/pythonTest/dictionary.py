dict1 = {
	'name': 'runoob', 
	'likes': 123, 
	'url': 'www.runoob.com'
	}
print(type(dict1))
print(dict1)
print(dict1['url'])

 
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
 
del tinydict['Name'] # 删除键 'Name'
tinydict.clear()     # 清空字典
del tinydict         # 删除字典
 
# print ("tinydict['Age']: ", tinydict['Age'])
# print ("tinydict['School']: ", tinydict['School'])

listdemo = ['Google','Runoob', 'Taobao']
newdict = {key:len(key) for key in listdemo}
print(newdict)