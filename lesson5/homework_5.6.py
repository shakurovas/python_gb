import re


def searching_elems(reg_exp, lesson_item):
    result1 = re.match(reg_exp, lesson_item)
    if result1:
        result1_2 = re.split(r'\(', result1[0])
        return int(result1_2[0])


final_dict = {'Informatics': 0,
              'Physics': 0,
              'Physical education': 0}
my_list = []

with open('test5.6.txt') as file:
    lessons = (file.readlines())
    for lesson in lessons:
        lesson = (lesson.replace('\n', '')).split(' ')
        sum_res = 0
        for item in lesson:
            if searching_elems(r'\d+\(l\)', item):
                sum_res += searching_elems(r'\d+\(l\)', item)
            if searching_elems(r'\d+\(pr\)', item):
                sum_res += searching_elems(r'\d+\(pr\)', item)
            if searching_elems(r'\d+\(lab\)', item):
                sum_res += searching_elems(r'\d+\(lab\)', item)
        print(sum_res)
        my_list.append(sum_res)

print('Total: ', dict(zip(final_dict, my_list)))
