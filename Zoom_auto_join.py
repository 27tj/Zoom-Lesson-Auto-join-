from zoom_auto_join_lib import *
num_of_lesson = int(input("Enter numbers of lesson:"))
lesson_pwd = []
lesson_start = []
lesson_end = []
lesson_id = []
to_user_: str = "Enter lesson {0} {1} {2}:"
for i in range(0, num_of_lesson):
    lesson_start.append(input(to_user_.format(i + 1, "start time", "(HH:MM:SS UTC)")))
    lesson_end.append(input(to_user_.format(i + 1, "end time", "(HH:MM:SS UTC)")))
    lesson_id.append(input(to_user_.format(i + 1, "id", "")))
    lesson_pwd.append(input(to_user_.format(i + 1, "password", "")))
for i in range(0, num_of_lesson):
    print("output:", lesson_start[i], lesson_end[i], lesson_id[i], lesson_pwd[i])
    lesson(lesson_start[i], lesson_end[i], lesson_id[i], lesson_pwd[i])


