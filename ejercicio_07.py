#Sistema de calificaciones con curva
student1_user = str(input("Introduce el nombre del estudiante 1: "))
grade1_student1 = float(input("Introduce la nota 1 para estudiante 1:" ))
grade2_student1 = float(input("Introduce la nota 2 para estudiante 1:"))
grade3_student1 = float(input("Introduce la nota 3 para estudiante 1:"))
promedio_student1 = (grade1_student1 + grade2_student1 + grade3_student1) / 3

student2_user = str(input("Introduce el nombre del estudiante 2: "))
grade1_student2 = float(input("Introduce la nota 1 para estudiante 2:" ))
grade2_student2 = float(input("Introduce la nota 2 para estudiante 2:"))
grade3_student2 = float(input("Introduce la nota 3 para estudiante 2:"))
promedio_student2 = (grade1_student2 + grade2_student2 + grade3_student2) / 3

student3_user = str(input("Introduce el nombre del estudiante 3: "))
grade1_student3 = float(input("Introduce la nota 1 para estudiante 3:" ))
grade2_student3 = float(input("Introduce la nota 2 para estudiante 3:"))
grade3_student3 = float(input("Introduce la nota 3 para estudiante 3:"))
promedio_student3 = (grade1_student3 + grade2_student3 + grade3_student3) / 3

student4_user = str(input("Introduce el nombre del estudiante 4: "))
grade1_student4 = float(input("Introduce la nota 1 para estudiante 4:" ))
grade2_student4 = float(input("Introduce la nota 2 para estudiante 4:"))
grade3_student4 = float(input("Introduce la nota 3 para estudiante 4:"))
promedio_student4 = (grade1_student4 + grade2_student4 + grade3_student4) / 3

student5_user = str(input("Introduce el nombre del estudiante 5: "))
grade1_student5 = float(input("Introduce la nota 1 para estudiante 5:" ))
grade2_student5 = float(input("Introduce la nota 2 para estudiante 5:"))
grade3_student5 = float(input("Introduce la nota 3 para estudiante 5:"))
promedio_student5 = (grade1_student5 + grade2_student5 + grade3_student5) / 3

curva_student = False
if promedio_student1 < 70 and promedio_student2 < 70 and promedio_student3 < 70 and promedio_student4 < 70 and promedio_student5 < 70:
    curva_student = True

print("Calificaciones mmodificandose")

if curva_student:
    print("Todos los estudiantes tienen promedio menor de 70. Aplicando curva de +5 puntos.")
    curva1_student1 = min(grade1_student1 + 5, 100)
    curva2_student1 = min(grade2_student1 + 5, 100)
    curva3_student1 = min(grade3_student1 + 5, 100)
    promedio_curva1 = (curva1_student1 + curva2_student1 + curva3_student1) / 3

    curva1_student2 = min(grade1_student2 + 5, 100)
    curva2_student2 = min(grade2_student2 + 5, 100)
    curva3_student2 = min(grade3_student2 + 5, 100)
    promedio_curva2 = (curva1_student2 + curva2_student2 + curva3_student2) / 3

    curva1_student3 = min(grade1_student3 + 5, 100)
    curva2_student3 = min(grade2_student3 + 5, 100)
    curva3_student3 = min(grade3_student3 + 5, 100)
    promedio_curva3 = (curva1_student3 + curva2_student3 + curva3_student3) / 3

    curva1_student4 = min(grade1_student4 + 5, 100)
    curva2_student4 = min(grade2_student4 + 5, 100)
    curva3_student4 = min(grade3_student4 + 5, 100)
    promedio_curva4 = (curva1_student4 + curva2_student4 + curva3_student4) / 3

    curva1_student5 = min(grade1_student5 + 5, 100)
    curva2_student5 = min(grade2_student5 + 5, 100)
    curva3_student5 = min(grade3_student5 + 5, 100)
    promedio_curva5 = (curva1_student5 + curva2_student5 + curva3_student5) / 3
else:
    print("No se aplica curva, ya que no todos los estudiantes tienen promedio menor de 70.")
    promedio_curva1 = promedio_student1
    promedio_curva2 = promedio_student2
    promedio_curva3 = promedio_student3
    promedio_curva4 = promedio_student4
    promedio_curva5 = promedio_student5

print("Tabla final")
print(student1_user, promedio_curva1)
print(student2_user, promedio_curva2)
print(student3_user, promedio_curva3)
print(student4_user, promedio_curva4)
print(student5_user, promedio_curva5)

