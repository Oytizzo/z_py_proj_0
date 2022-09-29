import json

with open('sauto_schedules.json', 'r') as sauto_schedules_content:
    student_schedules = json.load(sauto_schedules_content)

with open('tauto_schedules.json', 'r') as tauto_schedules_content:
    teacher_schedules = json.load(tauto_schedules_content)


def is_matched(list1, list2):
    attributes_to_match = ["scheduleID", "subject", "subjectWeek", "subjectLevel", "startTime", "endTime",
                           "test"]
    for i in range(len(list1)):
        for j in range(len(list1[i])):
            for attr in attributes_to_match:
                if list1[i][j][attr] == list2[i][j][attr]:
                    print(f"Matched {attr} {list2[i][j][attr]} between student and teacher")

    return True


def student_teacher_retrieved_schedules(student_schedules, teacher_schedules):
    study_content_from_student = []
    study_content_from_teacher = []
    for student_each_data in student_schedules['data']:
        for teacher_each_data in teacher_schedules['data']:
            if student_each_data['classScheduledDate'] == teacher_each_data['classScheduledDate']:
                # grab student studycontent
                student_study_contents_from_student = student_each_data['studyContent']

                # grab teacher all students study content of same student name
                students_from_teacher_schedules_on_that_day = []
                for each_item in teacher_each_data['time30DaysList']:
                    for each_item_in_student in each_item['students']:
                        students_from_teacher_schedules_on_that_day.append(each_item_in_student)

                student_study_contents_from_teacher = []
                for student in students_from_teacher_schedules_on_that_day:
                    if student['studentName'] == student_each_data['studentName']:
                        student_study_contents_from_teacher.append(student)
                # compare the attributes
                # print(student_study_contents_from_student)
                # print(student_study_contents_from_teacher)
                study_content_from_student.append(student_study_contents_from_student)
                study_content_from_teacher.append(student_study_contents_from_teacher)

                break
            else:
                continue
    print(study_content_from_student)
    print(study_content_from_teacher)
    with open('sauto.json', 'w') as sauto:
        json.dump(study_content_from_student, sauto, indent=4)

    with open('tauto.json', 'w') as tauto:
        json.dump(study_content_from_teacher, tauto, indent=4)

    return study_content_from_student, study_content_from_teacher


def main(student_schedules, teacher_schedules):
    return is_matched(*student_teacher_retrieved_schedules(student_schedules, teacher_schedules))


if __name__ == "__main__":
    main(student_schedules, teacher_schedules)
