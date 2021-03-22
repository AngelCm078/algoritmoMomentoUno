"""
Una institución educativa se encuentra en proceso de finalizar semestre y en proceso de admisión para el próximo semestre. La institución requiere un software que le permita solucionar estas dos problemáticas con las siguientes restricciones. 
Para finalización de semestre: 
Se desean subir las notas de los alumnos al sistema de los programas que se asignen por el Docente, se le pide el número de alumnos, nombre de cada alumno, programa académico, si es hombre o mujer, además, las 5 notas obtenidas durante el curso. El software calcula el promedio de las 5 notas. Al finalizar la ejecución debe mostrar cuántos hombres y mujeres hay en cada programa académico, el promedio de notas por cada programa y el listado de alumnos con el respectivo promedio de cada uno.
Para el proceso de admisión 
La institución requiere que se le muestre cuántos estudiantes en total se matricularon y el promedio de edad de los matriculados, además, requiere saber cuántos hombres y mujeres se matricularon.
El proceso de admisión termina hasta que el usuario decida que ya no se van a matricular más personas.
"""
# Funcion para validar opcion de lo que se desea haga el programa
def menu():
    validado = False
    menu=0

    while(not validado):
        try:
            menu = int(input("-"))  
            if menu<1 or menu>2:
                print("Ingrese opcion valida.")
                validado=False
            else:         
                validado = True
        except ValueError:
            print("Ingrese opcion valida.")
    
    return menu

#Funcion de validacion de notas entre 0 y 5, y que no ingrese valor vacio
def validarNotas():
    validado = False
    nota=0

    while(not validado):
        try:
            nota = float(input("Ingrese Nota: "))   
            if nota<0 or nota>5:
                print("Ingrese Nota entre 0 y 5.")
                validado=False
            else:         
                validado = True
        except ValueError:
            print("Ingrese Nota entre 0 y 5.")
    
    return nota


#Funcion para validar el Ingreso mayor a 0 o campo vacio de cantidad de Alumnos
def cantidadEstudiantes():
    validado = False
    num=0

    while(not validado):
        try:
            num = int(input("Ingrese cantidad de alumnos: "))
            validado = True
        except ValueError:
            print("Ingrese cantidad mayor a 0.")
    
    return num

# Funcion para encontrar promedio de notas de cada alumno
def averageStudent():
    average = 0
    for j in range(1, 6):       
        average = average + validarNotas()             
    average = average / 5
    return average


#Funcion de validacion de edad entre 15 y 55, y que no ingrese valor vacio
def validarEdad():
    validado = False
    edad=0

    while(not validado):
        try:
            edad = int(input("Ingrese Edad: "))   
            if edad<15 or edad>55:
                print("Ingrese Edad entre 15 y 55.")
                validado=False
            else:         
                validado = True
        except ValueError:
            print("Ingrese Edad entre 15 y 55.")
    
    return edad


#Variables Globales
asignatura = []
infoStudent = []
contMujeres = 0
contHombres = 0
averageEdad = 0


#Inicio programa
print("Bienvenido\n que desea Hacer:\n 1 - Ingresar Notas\n 2 - Matricular Estudiantes")
menu = menu()

if menu == 1:
    while True:
        stopProgram = input("¿Desea ingresar un programa académico?, N-no, S-si: ")

        if stopProgram == "N" or stopProgram == "n":
            break
        elif stopProgram == "S" or stopProgram == "s":

            while True:
                program = input("Ingrese programa académico: ")

                if program == "":
                    print("¡Programa no valido!")
                else:
                    asignatura.append(program)
                    break
        else:
            print("Ingrese una Opcion Valida")

    if len(asignatura) > 0:

        while True:

            numAlumnos = cantidadEstudiantes()

            if numAlumnos > 0:
                for i in range(numAlumnos):
                    print("-----------------------------------------")
                    nameStudent = input("Ingrese el nombre del alumno: ")

                    while True:

                        print("Ingrese una de estas opciones")
                        for j in asignatura:
                            print(f"-{j}")
                        print("-------------------------")

                        asignStudent = input()

                        if asignStudent in asignatura:
                            while True:
                                print("-----------------------------------------")
                                sex = input(
                                    "Ingrese el sexo: M-Mujer o H-Hombre: ")

                                if sex == "m" or sex == "M":
                                    break
                                elif sex == "h" or sex == "H":
                                    break
                                else:
                                    print("Opcion no valida.")

                            average = averageStudent()

                            infoStudent.append(
                                {"name": nameStudent, "asignatura": asignStudent, "sex": sex, "average": average})
                            break
                        else:
                            print("No Valida.")
                break
            else:
                print("Ingrese cantidad mayor a 0.")


        #Buscar y comparar Mujeres y hombres por cada asignatura ingresada por el docente y dar informe del promedio de cada asignatura.
        for j in range(0, len(asignatura)):  

            stM=0
            stH=0
            averageAsignatura = 0      

            for q in infoStudent:
                if asignatura[j] == q['asignatura'] and q['sex'] == "m" or q['sex'] == "M":           
                    stM += 1
                    averageAsignatura = averageAsignatura + q['average']

                elif asignatura[j] == q['asignatura'] and q['sex'] == "h" or q['sex'] == "H":           
                    stH += 1
                    averageAsignatura = averageAsignatura + q['average']
                
            print("-----------------------------------------")
            
            if averageAsignatura > 0:
                print(f"Promedio de {asignatura[j]}: {averageAsignatura/(stM+stH)}")
            else:
                print(f"Promedio de {asignatura[j]}: 0")
            
            print(f"Mujeres en {asignatura[j]}: {stM}")
            
            print(f"Hombres en {asignatura[j]}: {stH}")  

        
        print("-------------------------") 
        print("Lista de Alumnos")

        #Extraer la lista de los nombres y promedios de cada alumno
        for j in infoStudent:
            print("-------------------------")        
            print(f"Nombre: {j['name']}")
            print(f"Promedio: {j['average']}")
            
        print("-------------------------")   
        print("Fin del Programa")

    else:
        print("-------------------------") 
        print("Fin del Programa")
else:
    while True:      

        stopP = input("¿Matricular estudiante?\n S-si o N-no: ")

        if stopP == "n" or stopP == "N":
            print("-------------------------")
            break
        elif stopP == "s" or stopP == "S":            
            averageEdad = averageEdad + validarEdad()
            while True:                                    
                sex = input(
                    "Ingrese el sexo: M-Mujer u H-Hombre: ")

                if sex == "m" or sex == "M":

                    contMujeres += 1
                    break
                elif sex == "h" or sex == "H":

                    contHombres += 1
                    break
                else:
                    print("Opcion no valida.")
        else:
            print("Ingrese una opcion Valida")
    
    print(f"Total de Estudiantes Matriculados: {contHombres+contMujeres}")
    if (contHombres+contMujeres) == 0:
        print(f"Promedio edad de los estudiantes: 0")
    else:
        print(f"Promedio edad de los estudiantes: {averageEdad/(contHombres+contMujeres)}")
    print(f"Total Mujeres Matriculadas: {contMujeres}")
    print(f"Total Hombres Matriculados: {contHombres}")

    print("--------------------------------------")   
    print("Fin del Programa")

