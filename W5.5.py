import random
def generate_student_data(n_students, courses, cities, random_seed=42):
    '''Create a list of dict with dictionaries representing each attributes of each student.'''
    random.seed(random_seed)
    return [
      {
        "rollno": i, "city": random.choice(cities), 
        **{course: random.randint(1,100) for course in courses} 
      }
      for i in range(1,n_students+1)
    ]
def groupby(data:list, key:callable):
    '''Given a list of items, and a key, create a dictionary with the key as key function called 
    on item and the list of items with the same key as the corresponding value. 
    The order of items in the group should be the same order in the original list'''
    data_dict = {}
    for item in data:
        k = key(item)
        if k not in data_dict:
            data_dict[k] = []
        data_dict[k].append(item)
    return data_dict


def apply_to_groups(groups:dict, func:callable):
    '''Apply a function to the list of items for each group.'''
    result = {}
    for key, group in groups.items():
        result[key] = func(group)
    return result


def min_course_marks(student_data, course):
    '''Return the min marks on a given course'''
    course_marks = list(map(lambda student: student.get(course), student_data))
    course_marks = list(filter(lambda x: x is not None, course_marks))
    return min(course_marks) if course_marks else None


def max_course_marks(student_data, course):
    '''Return the max marks on a given course'''
    course_marks = list(map(lambda student: student.get(course), student_data))
    course_marks = list(filter(lambda x: x is not None, course_marks))
    return max(course_marks) if course_marks else None


def rollno_of_max_marks(student_data, course):
    '''Return the rollno of student with max marks in a course'''
    max_marks = max(list(map(lambda student: student.get(course), student_data)))
    return list(filter(lambda student: student.get(course) == max_marks, student_data))[0]["rollno"]


def sort_rollno_by_marks(student_data, course1, course2, course3):
    '''Return a sorted list of rollno sorted based on their marks on the three course marks. 
    course1 is compared first, then course2, then course3 to break ties.
    Hint: use tuples comparision'''
    sorted_students = sorted(student_data, key=lambda student: (student.get(course1), student.get(course2), student.get(course3)))
    return list(map(lambda student: student["rollno"], sorted_students))


def count_students_by_cities(student_data):
    '''Create a dictionary with city as key and number of students from each city as value.'''
    city_count = {}
    list(map(lambda student: city_count.update({student.get('city'): city_count.get(student.get('city'), 0) + 1}) if student.get('city') else None, student_data))
    return city_count


def city_with_max_no_of_students(student_data):
    '''Find the city with the maximum number of students.'''
    city_count = count_students_by_cities(student_data)
    return max(city_count, key = city_count.get)


def group_rollnos_by_cities(student_data):
    '''Create a dictionary with city as key and 
    a sorted list of rollno of students that belong to 
    that city as the value.'''
    city_rollnos = {}
    list(map(lambda student: city_rollnos.update({student.get('city'): city_rollnos.get(student.get('city'), []) + [student.get('rollno')]}) if student.get('city') else None, student_data))
    city_rollnos = {city: sorted(rollnos) for city, rollnos in city_rollnos.items()}
    return city_rollnos


def city_with_max_avg_course_mark(student_data, course):
    '''Find the city with the maximum avg course marks.'''
    city_marks = {}
    list(map(lambda student: city_marks.update({student.get('city'): city_marks.get(student.get('city'), []) + [student.get(course)]}) if student.get('city') and student.get(course) else None, student_data))
    city_marks = {city: sum(marks) / len(marks) for city, marks in city_marks.items()}
    return max(city_marks, key=city_marks.get)