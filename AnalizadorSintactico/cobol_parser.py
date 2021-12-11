#------------------------ Se importan las librerias necesarias
import sys
import ply.yacc as yacc
from cobol_lexer import tokens #Se importan los tokens declarados en el analizador lexico.
VERBOSE = 1


#-------------------------------A continuación se declaran varias funciones las cuales nos servirán para poder validar los errores sintacticos.
#-------------------------------En este apartado se hace uso de los tokens que fueron declarados en el analizador lexico.
#------------------------Definicion de cabezera general de un programa en COBOL
def p_program(p):
    'program : cobol_source_program'
    pass
#------------------------ Estructura de un programa COBOL
def p_cobol_source_program(p):
    '''cobol_source_program : cobol_identification_division cobol_source_program
							| cobol_source_program cobol_enviroment_division cobol_source_program
							| cobol_source_program cobol_data_division cobol_source_program
							| cobol_source_program cobol_procedure_division nested_cobol_source_program cobol_source_program
							| cobol_end_program
    '''		
    pass
#------------------------ Estructura del Identification Division
def p_cobol_identification_division(p):
    '''cobol_identification_division : IDENTIFICATION DIVISION PUNTO program_id_cobol_source_program identification_division_content
										| ID DIVISION PUNTO program_id_cobol_source_program identification_division_content
    '''		
    pass
#------------------------ Estructura del Enviroment Division
def p_cobol_enviroment_division(p):
    '''cobol_enviroment_division : ENVIRONMENT DIVISION PUNTO enviroment_division_content
								| empty
    '''		
    pass
#------------------------ Estructura del Data Division
def p_cobol_data_division(p):
    '''cobol_data_division : DATA DIVISION PUNTO data_division_content
							| empty
    '''		
    pass
#------------------------ Estructura del Procedure Division
def p_cobol_procedure_division(p):
    '''cobol_procedure_division : procedure_division
    '''		
    pass
#------------------------ Estructura del End Program
def p_cobol_end_program(p):
    '''cobol_end_program : END PROGRAM VARIABLE PUNTO
							| empty
    '''		
    pass

#------------------------ Se define la sintaxis de declaracion del nombre del programa
def p_program_id_cobol_source_program(p):
	'''program_id_cobol_source_program : PROGRAM_ID PUNTO VARIABLE PUNTO
							
	'''
	pass
#
#COLOCAR ID DIVIDION Y IDENT... DIVISION
def p_nested_cobol_source_program(p):
    '''nested_cobol_source_program : IDENTIFICATION DIVISION PUNTO program_id_nested_cobol_source_program identification_division_content ENVIRONMENT DIVISION PUNTO enviroment_division_content DATA DIVISION PUNTO data_division_content procedure_division nested_cobol_source_program END PROGRAM VARIABLE PUNTO
									| empty
    '''		
    pass
#------------------------ Se declara una función que nos servirá para validar los nombres del programa
def p_program_id_nested_cobol_source_program(p):
	'''program_id_nested_cobol_source_program : PROGRAM_ID PUNTO VARIABLE PUNTO
	'''
	pass

#------------------------ Se declara una función que nos servirá para validar el contenido de la descripcion del programa
def p_identification_division_content(p):
	'''identification_division_content : AUTHOR PUNTO VARIABLE PUNTO identification_division_content
							| identification_division_content INSTALLATION PUNTO VARIABLE PUNTO
							| identification_division_content DATE_WRITTEN PUNTO VARIABLE PUNTO
							| identification_division_content DATE_COMPILED PUNTO VARIABLE PUNTO
							| identification_division_content SECURITY PUNTO VARIABLE PUNTO
							| empty
	'''
	pass
#------------------------ Se declara una función que nos servirá para validar la seccion del entorno de division
# QUITADO imput_output_section de la funcion de abajo
def p_enviroment_division_content(p):
	'''enviroment_division_content : configuration_section
	'''
	pass
#------------------------ Se declara una función que nos servirá para validar la declaracion de la seccion de configuracion
def p_configuration_section(p):
	'''configuration_section : CONFIGURATION SECTION PUNTO
							| CONFIGURATION SECTION PUNTO configuration_section_paragrahs
							| empty
	'''
	pass
#------------------------ Se declara una función que nos servirá para validar el contenido de la seccion de configuracion
def p_configuration_section_paragrahs(p):
	'''configuration_section_paragrahs : source_computer_paragraph object_computer_paragraph special_names_paragraph
	'''
	pass
#------------------------ Se declara una función que nos servirá para validar la sentencia source computer
def p_source_computer_paragraph(p):
	'''source_computer_paragraph : SOURCE_COMPUTER PUNTO VARIABLE PUNTO 
								| empty
	'''
	pass
#------------------------ Se declara una función que nos servirá para validar la sentencia object computer
def p_object_computer_paragraph(p):
	'''object_computer_paragraph : OBJECT_COMPUTER PUNTO VARIABLE PUNTO
								| empty
	'''
	pass
#------------------------ Se declara una función que nos servirá para validar las variables especiales
def p_special_names_paragraph(p):
	'''special_names_paragraph : SPECIAL_NAMES PUNTO VARIABLE PUNTO
								| empty
	'''
	pass

"""def p_imput_output_section(p):
	'''special_names_paragraph : SPECIAL_NAMES PUNTO VARIABLE PUNTO
								|empty
	'''
	pass"""
#------------------------ Se declara una función que nos servirá para validar el data division
#pueden aparecer las tres secciones
def p_data_division_content(p):
	'''data_division_content : WORKING_STORAGE SECTION PUNTO data_item_entry 
								| FILE SECTION PUNTO data_file_entry
								| FILE SECTION PUNTO WORKING_STORAGE SECTION PUNTO data_item_entry
								| empty
	'''
	pass
#------------------------ Se declara una función que nos servirá para validar el contenido del data_division
def p_data_item_entry(p):
	'''data_item_entry : stament_declaration_var
						| data_item_entry stament_declaration_var
						| empty
	'''
	pass
#Se declara una función que nos servirá para validar el file entry
def p_data_file_entry(p):
	'''data_file_entry : empty
	'''
	pass
#------------------------ Se declara una función que nos servirá para validar la declaracion de variables
def p_stament_declaration_var(p):
	'''stament_declaration_var : stament_declaration_var NUMERO VARIABLE PIC NUMERO PARENT_IZQ NUMERO PARENT_DER PUNTO
								| stament_declaration_var NUMERO VARIABLE PIC VARIABLE PARENT_IZQ NUMERO PARENT_DER PUNTO
								| stament_declaration_var NUMERO VARIABLE PICTURE VARIABLE PARENT_IZQ NUMERO PARENT_DER PUNTO
								| stament_declaration_var NUMERO VARIABLE PIC VARIABLE PARENT_IZQ NUMERO PARENT_DER PUNTO VALUE STRING
								| stament_declaration_var NUMERO VARIABLE PIC VARIABLE PUNTO
								| stament_declaration_var NUMERO VARIABLE PIC NUMERO PUNTO
								| NUMERO VARIABLE PIC NUMERO PARENT_IZQ NUMERO PARENT_DER PUNTO
								| NUMERO VARIABLE PIC VARIABLE PARENT_IZQ NUMERO PARENT_DER PUNTO
								| NUMERO VARIABLE PICTURE VARIABLE PARENT_IZQ NUMERO PARENT_DER PUNTO
								| NUMERO VARIABLE PIC VARIABLE PARENT_IZQ NUMERO PARENT_DER PUNTO VALUE STRING
								| NUMERO VARIABLE PIC VARIABLE PUNTO
								| NUMERO VARIABLE PIC NUMERO PUNTO
	'''
	pass
#------------------------ Se declara una función que nos servirá para validar la seccion de procedimientos
def p_procedure_division(p):
	'''procedure_division : PROCEDURE DIVISION PUNTO paragrahps
							| PROCEDURE DIVISION PUNTO MAIN_PROCEDURE PUNTO paragrahps
							| PROCEDURE DIVISION PUNTO paragrahps STOP RUN PUNTO
							| PROCEDURE DIVISION PUNTO MAIN_PROCEDURE PUNTO paragrahps STOP RUN PUNTO
	'''
	pass
#------------------------ Se declara una función que nos servirá para validar el contenido de la seccion de procedimientos
def p_paragrahps(p):
	'''paragrahps : paragrahps statements
					| statements
					| empty
	'''
	pass
#------------------------ Se declara una función que nos servirá para validar las sentencias aceptadas en la seccion de procedimeintos
def p_statements(p):
	'''statements : stm_display
					| stm_acept
					| stm_add
					| stm_divide
					| stm_multiply
					| stm_minus
					| if_statement
	'''
	pass
#------------------------ Se declara una función que nos servirá para validar los displays
def p_stm_display(p):
	'''stm_display : DISPLAY STRING PUNTO
					| DISPLAY STRING VARIABLE PUNTO 
					| DISPLAY STRING WITH NO ADVANCING PUNTO
					| DISPLAY VARIABLE STRING PUNTO
					| DISPLAY STRING FUNCTION LENGTH PARENT_IZQ VARIABLE PARENT_DER PUNTO
					| DISPLAY STRING PUNTO stm_display 
					| DISPLAY STRING WITH NO ADVANCING PUNTO stm_display 
					| DISPLAY STRING VARIABLE PUNTO stm_display 
					| DISPLAY VARIABLE STRING PUNTO stm_display 
					| DISPLAY STRING FUNCTION LENGTH PARENT_IZQ VARIABLE PARENT_DER PUNTO stm_display 
	'''
	pass
#------------------------ Se declara una función que nos servirá para validar la sentencia acept
def p_stm_acept(p):
	'''stm_acept : ACCEPT VARIABLE PUNTO
					| ACCEPT VARIABLE PUNTO stm_acept
	'''
	pass
#------------------------ Se declara una función que nos servirá para validar la expresion de suma
def p_stm_add(p):
	'''stm_add : ADD VARIABLE TO VARIABLE GIVING VARIABLE PUNTO
				| ADD VARIABLE TO VARIABLE PUNTO
	'''
	pass
#------------------------ Se declara una función que nos servirá para validar la expresion de division
def p_stm_divide(p):
	'''stm_divide : DIVIDE VARIABLE INTO VARIABLE GIVING VARIABLE PUNTO
				| DIVIDE VARIABLE INTO VARIABLE PUNTO
	'''
	pass
#------------------------ Se declara una función que nos servirá para validar la expresion de multiplicacion
def p_stm_multiply(p):
	'''stm_multiply : MULTIPLY VARIABLE BY VARIABLE GIVING VARIABLE PUNTO
					| MULTIPLY VARIABLE BY VARIABLE PUNTO
	'''
	pass
#------------------------ Se declara una función que nos servirá para validar la expresion de resta
def p_stm_minus(p):
	'''stm_minus : SUBTRACT VARIABLE FROM VARIABLE GIVING VARIABLE PUNTO
				| SUBTRACT VARIABLE FROM VARIABLE PUNTO
	'''
	pass
#------------------------ Se declara una función que nos servirá para validar la estructura if
def p_if_statement(p):
	'''if_statement : IF conditional ifthen ifelse END_IF
					| IF conditional ifthen
					| IF conditional ifthen ifelse
					| IF conditional ifthen END_IF
	'''
	pass
#------------------------ Se declara una función que nos servirá para validar la estructura ifthen
def p_ifthen(p):
	'''ifthen : THEN NEXT SENTENCE
				| THEN statements
				| statements
				| NEXT SENTENCE
	'''
	pass
#------------------------ Se declara una función que nos servirá para validar la estructura ifelse
def p_ifelse(p):
	'''ifelse : ELSE NEXT SENTENCE
				| ELSE statements
	'''
	pass
#------------------------ Se declara una función que nos servirá para validar la estructura del condicional
def p_conditional(p):
	'''conditional : PARENT_IZQ aritmeticExpresion PARENT_DER
				| PARENT_IZQ logicExpresion PARENT_DER
				| aritmeticExpresion
				| logicExpresion
	'''
	pass
#------------------------ Se declara una función que nos servirá para validar la estructura de las expresiones aritmeticas
def p_aritmeticExpresion(p):
	'''aritmeticExpresion : VARIABLE MENOR_IGUAL VARIABLE
						| VARIABLE MAYOR_IGUAL VARIABLE
						| VARIABLE ES_IGUAL VARIABLE
						| VARIABLE MENOR_QUE VARIABLE
						| VARIABLE MAYOR_QUE VARIABLE
						| VARIABLE MENOR_IGUAL NUMERO
						| VARIABLE MAYOR_IGUAL NUMERO
						| VARIABLE ES_IGUAL NUMERO
						| VARIABLE MENOR_QUE NUMERO
						| VARIABLE MAYOR_QUE NUMERO
						| NUMERO MENOR_IGUAL VARIABLE
						| NUMERO MAYOR_IGUAL VARIABLE
						| NUMERO ES_IGUAL VARIABLE
						| NUMERO MENOR_QUE VARIABLE
						| NUMERO MAYOR_QUE VARIABLE
	'''
	pass
#------------------------ Se declara una función que nos servirá para validar la estructura de las expresiones logicas
def p_logicExpresion(p):
	'''logicExpresion : aritmeticExpresion AND aritmeticExpresion
				| aritmeticExpresion OR aritmeticExpresion
				| logicExpresion OR logicExpresion
				| logicExpresion AND logicExpresion
				| NOT VARIABLE
	'''
	pass
#------------------------ Se declara una función que nos servirá para validar los espacios vacios
def p_empty(p):
	'empty :'
	pass

#------------------------ Se declara una función que nos servirá para mostrar en consola los posibles errores detectados
def p_error(p):
    if VERBOSE:
        if p is not None:
            print (chr(27)+"[1;31m"+"\t ERROR: Error de sintaxis - Token Inesperado" + chr(27)+"[0m")
            print("\n" + "\t\tLinea: " + str(p.lexer.lineno) +"\t ---> " ,"Error sintactico de tipo {:4} en el valor {:4}".format(
            str(p.type), str(p.value)))
            #parser.errok()
        else:
            print (chr(27)+"[1;31m"+"\t Error durante la compilación: “Error de sintáxis”"+chr(27)+"[0m")
            print ("\t\tLinea:  "+str(p))
    else:
        raise Exception('syntax', 'error')


#------------------------ Se hace uso de la libreria yacc
parser = yacc.yacc('SLR')

script = 'prueba1.cbl' #En esta linea se agrega el nombre del archivo .cbl que se va analizar
scriptfile = open(script, 'r', encoding= 'UTF-8') #Con esta linea abrimos el archivo .cbl
scriptdata = scriptfile.read() #Con esta linea leemos el archivo .cbl
#print (scriptdata)

#------------------------ Finalmente se hace las impresiones correspondientes para mostrar si se detectaron errores o no en el programa analizado
print ("\n"+chr(27)+"[0;36m"+"INICIA ANALISIS SINTACTICO"+chr(27)+"[0m")
print("\n" + "\x1b[1;33m" + "ERRORES ENCONTRADOS:  ------------------------------------------- >\n")
parser.parse(scriptdata, tracking=True) #En esta parte se mostrarían los errores en caso de existir alguna
print (chr(27)+"[0;36m"+"FIN DEL ANALISIS SINTACTICO"+chr(27)+"[0m")


#------------------------ Se imprime los integrantes del equipo
print("Programa elaborado por:"+"\n"
        +"\t--> Luis Santiago Noh Cahum - 19070049"+"\n"
        +"\t--> Jesus Israel Gamboa Ake - 19070041"+"\n"
        +"\t--> Maricela del Rosario Puc Oy - 19070051"+"\n"
        +"\t--> Roger David Aban Ku - 19070025\n")