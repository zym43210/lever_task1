def creating_list_of_dicts(data_rooms, data_students):
    list_with_students = []
    room_composition = []

    for room_step in data_rooms:

        room_number = room_step["name"].split('#')
        dict_with_students = {"roomNumber": room_number[-1]}
        search_counter = 0

        for students_name in data_students:

            if students_name["room"] == int(room_number[-1]):
                room_composition.append(students_name["name"])
                del data_students[search_counter]

            search_counter += 1
        dict_with_students.update({"Names": room_composition})

        list_with_students.append(dict_with_students)
        room_composition = []
    return list_with_students
