import sys
import json
from xml.dom import minidom

class file_worker:
	@staticmethod
	def read_from_file(path):
		read_file=	open(path,"r")
		data = json.load(read_file)
		return data
	@staticmethod
	def write_to_file_json(object_for_dumping):
		with open("data_file.json", "w") as write_file:
			json.dump(object_for_dumping,write_file, sort_keys=True,indent=4)
	@staticmethod
	def write_to_file_xml(object_for_dumping):
		with open("minidom_example.xml", "w") as f:
	   		f.write(str(object_for_dumping))


class union_of_files:
	@staticmethod
	def creating_list_of_dicts(data_rooms,data_students):
		list_with_students=[]
		for room_number in data_rooms:
			res=room_number["name"].split('#')
			dict_with_students={"roomNumber":res[-1]}
			list_with_students.append(dict_with_students)
			for students_name in data_students:

				if students_name["room"]==int(res[-1]):
					dict_with_students.update({students_name["name"]:"name"})
		return list_with_students
			
		



data_rooms = file_worker.read_from_file(sys.argv[1])
data_students = file_worker.read_from_file(sys.argv[2])




if int(sys.argv[3])==1:
	file_worker.write_to_file_json(union_of_files.creating_list_of_dicts(data_rooms,data_students))
else:
	file_worker.write_to_file_xml(union_of_files.creating_list_of_dicts(data_rooms,data_students))