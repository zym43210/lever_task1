import json


read_file_rooms=open("rooms.json","r")
read_file_students=open("students.json","r")
data_rooms = json.load(read_file_rooms)
data_students = json.load(read_file_students)
studentslist_in_room=[]
list_with_students=[]

for room_number in data_rooms:
	res=room_number["name"].split('#')
	dict_with_students={"roomNumber":res[-1]}
	list_with_students.append(dict_with_students)
	for students_name in data_students:

		if students_name["room"]==int(res[-1]):
			dict_with_students.update({students_name["name"]:"name"})

with open("data_file.json", "w") as write_file:
    json.dump(list_with_students,write_file, sort_keys=True,indent=4)