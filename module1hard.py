grades=[[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students={'Johnny','Bilbo','Steve','Khendrik','Aaron'}
alfavit_students=list(students)
alfavit_students.sort()
sredniy_ball_student_1=sum(grades[0])/len(grades[0])
sredniy_ball_student_2=sum(grades[1])/len(grades[1])
sredniy_ball_student_3=sum(grades[2])/len(grades[2])
sredniy_ball_student_4=sum(grades[3])/len(grades[3])
sredniy_ball_student_5=sum(grades[4])/len(grades[4])
print(dict([[alfavit_students[0],sredniy_ball_student_1],[alfavit_students[1],sredniy_ball_student_2],[alfavit_students[2],sredniy_ball_student_3],[alfavit_students[3],sredniy_ball_student_4],[alfavit_students[4],sredniy_ball_student_5]]))
