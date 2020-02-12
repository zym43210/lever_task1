import args_parsing
import files_union
import file_worker
from xml.dom import minidom

args = args_parsing.parse_arguments()

data_rooms = file_worker.file_reader(args.rooms_path)
data_students = file_worker.file_reader(args.students_path)

if args.ended_format == 1:
    file_worker.json_writer(
        files_union.creating_list_of_dicts(data_rooms, data_students))
else:
    file_worker.xml_writer(
        files_union.creating_list_of_dicts(data_rooms, data_students))
