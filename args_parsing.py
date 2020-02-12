import argparse

def parse_arguments():
	parser = argparse.ArgumentParser(description='json parsing')
	parser.add_argument('rooms_path', type=str, help='input dir for rooms')
	parser.add_argument('students_path', type=str, help='input dir for students')
	parser.add_argument('ended_format', type=int, help='choice between json or xml')
	arguments = parser.parse_args()
	return arguments