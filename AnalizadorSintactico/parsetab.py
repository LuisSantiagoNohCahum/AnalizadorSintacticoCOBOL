
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'SLR'

_lr_signature = 'ACCEPT ACCESS ADD ADDRESS ADVANCING AFTER ALL ALPHABET ALPHABETIC ALPHABETIC_LOWER ALPHABETIC_UPPER ALPHANUMERIC_EDITED ALSO ALTER ALTERNATE AND AND_LOGICO ANY APHANUMERIC APOSTROFE APPLY ARE AREA AREAS ASCENDING ASIGNACION_DIVISION ASIGNACION_MULTI ASIGNACION_RESIDUO ASIGNACION_RESTA ASIGNACION_SUMA ASSIGN AT AUTHOR AUTO AUTOMATIC AUTOTERMINATE AUTO_SKIP BACKGROUND BACKGROUND_COLOR BACKGROUND_HIGH BACKGROUND_LOW BACKWARD BEEP BEFORE BELL BINARY BIND BLANK BLINK BLINKING BLOCK BOLD BOTTOM BY CALL CANCEL CD CF CH CHARACTER CHARACTERS CLASS CLOSE COBOL CODE CODE_SET COL COLLATING COLUMN COMA COMILLAS COMMA COMMENTS COMMENTS_C99 COMMUNICATION COMP COMPUTATIONAL COMPUTATIONAL_1 COMPUTATIONAL_2 COMPUTATIONAL_3 COMPUTATIONAL_4 COMPUTE COMP_1 COMP_2 COMP_3 COMP_4 COMP_6 CONFIGURATION CONSOLE CONTAINS CONTENT CONTINUE CONTROL CONTROLS CONVERSION CONVERT CONVERTING COPY CORCHETE_DER CORCHETE_IZQ CORR CORRESPONDING COUNT CRT CURRENCY CURSOR DATA DATE DATE_COMPILED DATE_WRITTEN DAY DAY_OF_WEEK DE DEBUG DEBUGGING DECIMAL_POINT DECLARATIVES DECREMENTO DEFAULT DELETE DELIMITED DELIMITER DEPENDING DESCENDING DESIGUAL DESIGUALDAD_ESTRICTA DESTINATION DETAIL DISABLE DISPLAY DISTINTO DIVIDE DIVISION DOS_PUNTOS DRAWN DUPLICATES DYNAMIC ECHO EGI ELSE EMI EMPTY_CHECK ENABLED END END_ACCEPT END_ADD END_CALL END_COMPUTE END_DELETE END_DIVIDE END_EVALUATEQ END_IF END_MULTIPLY END_OF_PAGE END_PERFORM END_READ END_RECEIVE END_RETURN END_REWRITE END_SEARCH END_START END_STRING END_SUBTRACT END_UNSTRING END_WRITE ENTER ENVIRONMENT EOL EOP EOS EQUAL ERASE ERROR ESCAPE ESI ES_IGUAL ET EVALUATE EVERY EXCEPTION EXCLUSIVE EXIT EXPONENTE EXTEND EXTERNAL FALSE FD FILE FILE_CONTROL FILE_ID FILE_PREFIX FILLER FINAL FIRST FOOTING FOR FOREGROUND_COLOR FOREGROUND_COLOUR FROM FULL FUNCTION GENERATE GIVING GLOBAL GO GOBACK GREATER GRID GROUP HASHTAG HEADING HIGH HIGHLIGHT HIGH_BALUE HIGH_VALUES IDENTIFICADOR IDENTIFICATION IF IGUAL IGUALDAD_ESTRICTA IN INCREMENTO INDEX INDEXED INDICATE INITIAL INITIALIZE INPUT INPUT_OUTPUT INSPECT INSTALLATION INTO INVALID IS I_O JUST JUSTIFIED KEY LABEL LAST LEADING LEFT LEFTLINE LENGTH LENGTH_CHECK LESS LIMIT LIMITS LINAGE LINES LINGAKE_COUNTER LINKAGE LLAVE_DER LLAVE_IZQ LOCK LOCK_HOLDING LOW LOWLIGHT LOW_VALUE LOW_VALUES MAIN_PROCEDURE MAS_IGUAL MAYOR_IGUAL MAYOR_QUE MEMORY MENOR_IGUAL MENOR_QUE MENOS_IGUAL MERGE MODE MODULES MOVE MULTIPLE MULTIPLICACION MULTIPLY NATIVE NEGATIVE NEXT NO NOT NOT_LOGICO NO_ECHO NUMBER NUMERIC NUMERIC_EDITED NUMERO OBJECT_COMPUTER OCCURS OF OFF OMITTED ON OPEN OPTIONAL OP_DIVISION OR ORDER ORGANIZATION OR_LOGICO OTHER OTHERS OUTPUT OVERFLOW OVERLINE PACKED_DECIMAL PADDING PAGE_COUNTER PARENT_DER PARENT_IZQ PERFORM PGE PIC PICTURE PLUS POINTER POS POSITION POSITIVE PREVIOUS PRINTING PRINT_CONTROL PROCEDURE PROCEDURES PROCEED PROGRAM PROGRAM_ID PROMPT PROTECTED PUNTO PUNTOYCOMA PURGE QUEUE QUOTE QUOTES RANDOM RD READ READERS RECEIVE RECORD RECORDING RECORDS REDEFINES REEL REFERENCE REFERENCES RELATIVE RELEASE REMAINDER REMOVAL RENAMES REPLACE REPLACING REPORT REPORTING REPORTS REQUIRED RERUN RESERVE RESIDUO RESTA RETUNRNIN RETURN RETURN_CODE RETURN_UNSIGNED REVERSE REVERSED REVERSE_VIDEO REWIND REWRITE RF RH RIGHT ROLLBACK RUN SAME SCREEN SD SEARCH SECTION SECURE SECURITY SEGMENT SEGMENT_LIMIT SELECT SEND SENTENCE SEPARATE SEQUENCE SEQUENTIAL SET SIGN SIZE SORT SORT_MERGE SOURCE SOURCE_COMPUTER SPACE SPACES SPECIAL_NAMES STANDARD START STATUS STOP STRING SUBTRACT SUMA SUPPRESS SYCHRONIZED SYMBOLIC SYNC TAB TALLYNG TAPE TERMINAL TERMINATE TEST TEXT THAN THEN THROUGH THRU TIME TIMES TO TOP TRAILING TRUE UNDERLINE UNDERLINED UNIT UNLOCK UNSTRING UNTIL UP UPDATE UPDATES UPON USAGE USE USING VALUE VALUES VARIABLE VARYING WHEN WITH WORDS WORKING_STORAGE WRITE WRITERS ZERO ZEROES ZEROScobol_source_program : IDENTIFICATION DIVISION PUNTO program_id_cobol_source_program identification_division_content ENVIRONMENT DIVISION PUNTO enviroment_division_content DATA DIVISION PUNTO data_division_content procedure_division nested_cobol_source_program END PROGRAM VARIABLE PUNTO\n    program_id_cobol_source_program : PROGRAM_ID PUNTO VARIABLE PUNTO\n\t\t\t\t\t\t\t\n\tnested_cobol_source_program : IDENTIFICATION DIVISION PUNTO program_id_nested_cobol_source_program identification_division_content ENVIRONMENT DIVISION PUNTO enviroment_division_content DATA DIVISION PUNTO data_division_content procedure_division nested_cobol_source_program END PROGRAM VARIABLE PUNTO\n\t\t\t\t\t\t\t\t\t| empty\n    program_id_nested_cobol_source_program : PROGRAM_ID PUNTO VARIABLE PUNTO\n\tidentification_division_content : AUTHOR PUNTO VARIABLE PUNTO identification_division_content\n\t\t\t\t\t\t\t| identification_division_content INSTALLATION PUNTO VARIABLE PUNTO\n\t\t\t\t\t\t\t| identification_division_content DATE_WRITTEN PUNTO VARIABLE PUNTO\n\t\t\t\t\t\t\t| identification_division_content DATE_COMPILED PUNTO VARIABLE PUNTO\n\t\t\t\t\t\t\t| identification_division_content SECURITY PUNTO VARIABLE PUNTO\n\t\t\t\t\t\t\t| empty\n\tenviroment_division_content : configuration_section\n\tconfiguration_section : CONFIGURATION SECTION PUNTO\n\t\t\t\t\t\t\t| CONFIGURATION SECTION PUNTO configuration_section_paragrahs\n\t\t\t\t\t\t\t| empty\n\tconfiguration_section_paragrahs : source_computer_paragraph object_computer_paragraph special_names_paragraph\n\tsource_computer_paragraph : SOURCE_COMPUTER PUNTO VARIABLE PUNTO \n\t\t\t\t\t\t\t\t| empty\n\tobject_computer_paragraph : OBJECT_COMPUTER PUNTO VARIABLE PUNTO\n\t\t\t\t\t\t\t\t| empty\n\tspecial_names_paragraph : SPECIAL_NAMES PUNTO VARIABLE PUNTO\n\t\t\t\t\t\t\t\t| empty\n\tdata_division_content : WORKING_STORAGE SECTION PUNTO data_item_entry \n\t\t\t\t\t\t\t\t| FILE SECTION PUNTO data_file_entry\n\t\t\t\t\t\t\t\t| FILE SECTION PUNTO WORKING_STORAGE SECTION PUNTO data_item_entry\n\t\t\t\t\t\t\t\t| empty\n\tdata_item_entry : stament_declaration_var \n\t\t\t\t\t\t| data_item_entry stament_declaration_var\n\t\t\t\t\t\t| empty\n\tdata_file_entry : empty\n\tstament_declaration_var : stament_declaration_var NUMERO VARIABLE PIC NUMERO PARENT_IZQ NUMERO PARENT_DER PUNTO\n\t\t\t\t\t\t\t\t| stament_declaration_var NUMERO VARIABLE PIC VARIABLE PARENT_IZQ NUMERO PARENT_DER PUNTO\n\t\t\t\t\t\t\t\t| stament_declaration_var NUMERO VARIABLE PICTURE VARIABLE PARENT_IZQ NUMERO PARENT_DER PUNTO\n\t\t\t\t\t\t\t\t| stament_declaration_var NUMERO VARIABLE PIC VARIABLE PARENT_IZQ NUMERO PARENT_DER PUNTO VALUE STRING\n\t\t\t\t\t\t\t\t| stament_declaration_var NUMERO VARIABLE PIC VARIABLE PUNTO\n\t\t\t\t\t\t\t\t| stament_declaration_var NUMERO VARIABLE PIC NUMERO PUNTO\n\t\t\t\t\t\t\t\t| empty\n\tprocedure_division : PROCEDURE DIVISION PUNTO paragrahps\n\t\t\t\t\t\t\t| PROCEDURE DIVISION PUNTO MAIN_PROCEDURE PUNTO paragrahps\n\tparagrahps : statements\n\t\t\t\t\t| paragrahps statements\n\t\t\t\t\t| paragrahps statements STOP RUN PUNTO\n\t\t\t\t\t| empty\n\tstatements : stm_display\n\t\t\t\t\t| stm_acept\n\t\t\t\t\t| stm_add\n\t\t\t\t\t| stm_divide\n\t\t\t\t\t| stm_multiply\n\t\t\t\t\t| stm_minus\n\t\t\t\t\t| empty\n\tstm_display : DISPLAY STRING PUNTO\n\t\t\t\t\t| DISPLAY STRING VARIABLE PUNTO\n\t\t\t\t\t| stm_display DISPLAY STRING PUNTO\n\t\t\t\t\t| stm_display DISPLAY STRING WITH NO ADVANCING PUNTO\n\t\t\t\t\t| stm_display DISPLAY STRING VARIABLE PUNTO\n\t\t\t\t\t| stm_display DISPLAY VARIABLE STRING PUNTO\n\t\t\t\t\t| stm_display DISPLAY STRING FUNCTION LENGTH PARENT_IZQ VARIABLE PARENT_DER PUNTO\n\t\t\t\t\t| empty\n\tstm_acept : ACCEPT VARIABLE PUNTO\n\t\t\t\t\t| stm_acept ACCEPT VARIABLE PUNTO\n\t\t\t\t\t| empty\n\tstm_add : ADD VARIABLE TO VARIABLE GIVING VARIABLE PUNTO\n\t\t\t\t| ADD VARIABLE TO VARIABLE PUNTO\n\tstm_divide : DIVIDE VARIABLE INTO VARIABLE GIVING VARIABLE PUNTO\n\t\t\t\t| DIVIDE VARIABLE INTO VARIABLE PUNTO\n\tstm_multiply : MULTIPLY VARIABLE BY VARIABLE GIVING VARIABLE PUNTO\n\t\t\t\t\t| MULTIPLY VARIABLE BY VARIABLE PUNTO\n\tstm_minus : SUBTRACT VARIABLE FROM VARIABLE GIVING VARIABLE PUNTO\n\t\t\t\t| SUBTRACT VARIABLE FROM VARIABLE PUNTO\n\tempty :'
    
_lr_action_items = {'IDENTIFICATION':([0,5,25,30,43,44,46,53,57,70,71,77,78,88,90,91,92,93,94,95,96,97,109,112,113,114,124,129,133,135,142,146,151,152,162,164,166,168,170,172,174,180,191,193,194,195,196,206,208,211,],[2,-70,-70,-70,-70,-70,-70,-70,66,-70,-70,-70,-70,-38,-40,-43,-44,-45,-46,-47,-48,-49,-70,-41,-50,-70,-70,-39,-51,-59,-70,-53,-60,-52,-42,-55,-56,-63,-65,-67,-69,-70,-54,-62,-64,-66,-68,-57,-70,66,]),'$end':([1,127,],[0,-1,]),'DIVISION':([2,11,40,58,66,143,200,],[3,18,42,69,75,160,205,]),'PUNTO':([3,6,8,12,13,14,15,17,18,23,26,27,28,29,41,42,47,54,59,60,62,65,69,73,75,84,89,107,110,111,117,118,130,132,134,144,145,148,150,153,154,155,156,157,158,160,181,183,184,185,186,197,198,199,201,205,215,],[4,10,16,19,20,21,22,24,25,30,35,36,37,38,43,44,56,64,70,71,72,74,77,85,86,108,114,124,126,127,133,135,146,151,152,161,162,164,166,168,170,172,174,176,178,180,191,193,194,195,196,202,203,204,206,208,216,]),'PROGRAM_ID':([4,86,],[6,110,]),'AUTHOR':([5,24,30,109,161,],[8,-2,8,8,-5,]),'END':([5,25,30,43,44,46,53,57,67,68,70,71,77,78,88,90,91,92,93,94,95,96,97,109,112,113,114,124,129,133,135,142,146,151,152,162,164,166,168,170,172,174,180,191,193,194,195,196,206,208,211,212,216,],[-70,-70,-70,-70,-70,-70,-70,-70,76,-4,-70,-70,-70,-70,-38,-40,-43,-44,-45,-46,-47,-48,-49,-70,-41,-50,-70,-70,-39,-51,-59,-70,-53,-60,-52,-42,-55,-56,-63,-65,-67,-69,-70,-54,-62,-64,-66,-68,-57,-70,-70,213,-3,]),'ENVIRONMENT':([5,7,9,24,25,30,35,36,37,38,39,43,44,46,53,57,70,71,77,78,88,109,114,124,125,129,142,161,180,208,211,],[-70,11,-11,-2,-70,-70,-7,-8,-9,-10,-6,-70,-70,-70,-70,-70,-70,-70,-70,-70,-70,-70,-70,-70,143,-70,-70,-5,-70,-70,-70,]),'INSTALLATION':([5,7,9,24,25,30,35,36,37,38,39,43,44,46,53,57,70,71,77,78,88,109,114,124,125,129,142,161,180,208,211,],[-70,12,-11,-2,-70,-70,-7,-8,-9,-10,12,-70,-70,-70,-70,-70,-70,-70,-70,-70,-70,-70,-70,-70,12,-70,-70,-5,-70,-70,-70,]),'DATE_WRITTEN':([5,7,9,24,25,30,35,36,37,38,39,43,44,46,53,57,70,71,77,78,88,109,114,124,125,129,142,161,180,208,211,],[-70,13,-11,-2,-70,-70,-7,-8,-9,-10,13,-70,-70,-70,-70,-70,-70,-70,-70,-70,-70,-70,-70,-70,13,-70,-70,-5,-70,-70,-70,]),'DATE_COMPILED':([5,7,9,24,25,30,35,36,37,38,39,43,44,46,53,57,70,71,77,78,88,109,114,124,125,129,142,161,180,208,211,],[-70,14,-11,-2,-70,-70,-7,-8,-9,-10,14,-70,-70,-70,-70,-70,-70,-70,-70,-70,-70,-70,-70,-70,14,-70,-70,-5,-70,-70,-70,]),'SECURITY':([5,7,9,24,25,30,35,36,37,38,39,43,44,46,53,57,70,71,77,78,88,109,114,124,125,129,142,161,180,208,211,],[-70,15,-11,-2,-70,-70,-7,-8,-9,-10,15,-70,-70,-70,-70,-70,-70,-70,-70,-70,-70,-70,-70,-70,15,-70,-70,-5,-70,-70,-70,]),'DATA':([5,25,30,31,32,34,43,44,45,46,48,53,55,57,61,63,70,71,74,77,78,85,88,108,109,114,124,129,142,180,190,208,211,],[-70,-70,-70,40,-12,-15,-13,-70,-14,-70,-18,-70,-20,-70,-16,-22,-70,-70,-17,-70,-70,-19,-70,-21,-70,-70,-70,-70,-70,-70,200,-70,-70,]),'OBJECT_COMPUTER':([5,25,30,43,44,46,48,53,57,70,71,74,77,78,88,109,114,124,129,142,180,208,211,],[-70,-70,-70,-70,-70,54,-18,-70,-70,-70,-70,-17,-70,-70,-70,-70,-70,-70,-70,-70,-70,-70,-70,]),'SPECIAL_NAMES':([5,25,30,43,44,46,48,53,55,57,70,71,74,77,78,85,88,109,114,124,129,142,180,208,211,],[-70,-70,-70,-70,-70,-70,-18,62,-20,-70,-70,-70,-17,-70,-70,-19,-70,-70,-70,-70,-70,-70,-70,-70,-70,]),'PROCEDURE':([5,25,30,43,44,46,49,52,53,57,70,71,77,78,79,80,81,83,88,104,105,109,114,124,129,142,176,178,180,202,203,204,208,209,210,211,],[-70,-70,-70,-70,-70,-70,58,-26,-70,-70,-70,-70,-70,-23,-27,-29,-24,-30,-70,-28,-37,-70,-70,-70,-70,-25,-36,-35,-70,-31,-32,-33,-70,-34,58,-70,]),'NUMERO':([5,25,30,43,44,46,53,57,70,71,77,78,79,80,88,104,105,109,114,124,129,140,142,175,176,177,178,179,180,202,203,204,208,209,211,],[-70,-70,-70,-70,-70,-70,-70,-70,-70,-70,-70,-70,106,-29,-70,106,-37,-70,-70,-70,-70,157,-70,187,-36,188,-35,189,-70,-31,-32,-33,-70,-34,-70,]),'DISPLAY':([5,25,30,43,44,46,53,57,70,71,77,78,88,90,91,92,93,94,95,96,97,109,112,113,114,124,129,133,135,142,146,151,152,162,164,166,168,170,172,174,180,191,193,194,195,196,206,208,211,],[-70,-70,-70,-70,-70,-70,-70,-70,-70,-70,98,-70,98,-40,-43,115,-45,-46,-47,-48,-49,-70,-41,-50,98,-70,98,-51,-59,-70,-53,-60,-52,-42,-55,-56,-63,-65,-67,-69,-70,-54,-62,-64,-66,-68,-57,-70,-70,]),'ACCEPT':([5,25,30,43,44,46,53,57,70,71,77,78,88,90,91,92,93,94,95,96,97,109,112,113,114,124,129,133,135,142,146,151,152,162,164,166,168,170,172,174,180,191,193,194,195,196,206,208,211,],[-70,-70,-70,-70,-70,-70,-70,-70,-70,-70,99,-70,99,-40,-43,-44,116,-46,-47,-48,-49,-70,-41,-50,99,-70,99,-51,-59,-70,-53,-60,-52,-42,-55,-56,-63,-65,-67,-69,-70,-54,-62,-64,-66,-68,-57,-70,-70,]),'ADD':([5,25,30,43,44,46,53,57,70,71,77,78,88,90,91,92,93,94,95,96,97,109,112,113,114,124,129,133,135,142,146,151,152,162,164,166,168,170,172,174,180,191,193,194,195,196,206,208,211,],[-70,-70,-70,-70,-70,-70,-70,-70,-70,-70,100,-70,100,-40,-43,-44,-45,-46,-47,-48,-49,-70,-41,-50,100,-70,100,-51,-59,-70,-53,-60,-52,-42,-55,-56,-63,-65,-67,-69,-70,-54,-62,-64,-66,-68,-57,-70,-70,]),'DIVIDE':([5,25,30,43,44,46,53,57,70,71,77,78,88,90,91,92,93,94,95,96,97,109,112,113,114,124,129,133,135,142,146,151,152,162,164,166,168,170,172,174,180,191,193,194,195,196,206,208,211,],[-70,-70,-70,-70,-70,-70,-70,-70,-70,-70,101,-70,101,-40,-43,-44,-45,-46,-47,-48,-49,-70,-41,-50,101,-70,101,-51,-59,-70,-53,-60,-52,-42,-55,-56,-63,-65,-67,-69,-70,-54,-62,-64,-66,-68,-57,-70,-70,]),'MULTIPLY':([5,25,30,43,44,46,53,57,70,71,77,78,88,90,91,92,93,94,95,96,97,109,112,113,114,124,129,133,135,142,146,151,152,162,164,166,168,170,172,174,180,191,193,194,195,196,206,208,211,],[-70,-70,-70,-70,-70,-70,-70,-70,-70,-70,102,-70,102,-40,-43,-44,-45,-46,-47,-48,-49,-70,-41,-50,102,-70,102,-51,-59,-70,-53,-60,-52,-42,-55,-56,-63,-65,-67,-69,-70,-54,-62,-64,-66,-68,-57,-70,-70,]),'SUBTRACT':([5,25,30,43,44,46,53,57,70,71,77,78,88,90,91,92,93,94,95,96,97,109,112,113,114,124,129,133,135,142,146,151,152,162,164,166,168,170,172,174,180,191,193,194,195,196,206,208,211,],[-70,-70,-70,-70,-70,-70,-70,-70,-70,-70,103,-70,103,-40,-43,-44,-45,-46,-47,-48,-49,-70,-41,-50,103,-70,103,-51,-59,-70,-53,-60,-52,-42,-55,-56,-63,-65,-67,-69,-70,-54,-62,-64,-66,-68,-57,-70,-70,]),'STOP':([5,25,30,43,44,46,53,57,70,71,77,78,88,90,91,92,93,94,95,96,97,109,112,113,114,124,129,133,135,142,146,151,152,162,164,166,168,170,172,174,180,191,193,194,195,196,206,208,211,],[-70,-70,-70,-70,-70,-70,-70,-70,-70,-70,-70,-70,-70,-40,-43,-44,-45,-46,-47,-48,-49,-70,128,-50,-70,-70,-70,-51,-59,-70,-53,-60,-52,-42,-55,-56,-63,-65,-67,-69,-70,-54,-62,-64,-66,-68,-57,-70,-70,]),'VARIABLE':([10,16,19,20,21,22,56,64,72,87,99,100,101,102,103,106,115,116,117,126,130,136,137,138,139,140,141,167,169,171,173,182,214,],[17,23,26,27,28,29,65,73,84,111,118,119,120,121,122,123,131,132,134,144,148,153,154,155,156,158,159,183,184,185,186,192,215,]),'CONFIGURATION':([25,180,],[33,33,]),'SECTION':([33,50,51,82,],[41,59,60,107,]),'SOURCE_COMPUTER':([43,],[47,]),'WORKING_STORAGE':([44,71,208,],[50,82,50,]),'FILE':([44,208,],[51,51,]),'PROGRAM':([76,213,],[87,214,]),'MAIN_PROCEDURE':([77,],[89,]),'STRING':([98,115,131,207,],[117,130,150,209,]),'TO':([119,],[136,]),'INTO':([120,],[137,]),'BY':([121,],[138,]),'FROM':([122,],[139,]),'PIC':([123,],[140,]),'PICTURE':([123,],[141,]),'RUN':([128,],[145,]),'WITH':([130,],[147,]),'FUNCTION':([130,],[149,]),'NO':([147,],[163,]),'LENGTH':([149,],[165,]),'GIVING':([153,154,155,156,],[167,169,171,173,]),'PARENT_IZQ':([157,158,159,165,],[175,177,179,182,]),'ADVANCING':([163,],[181,]),'PARENT_DER':([187,188,189,192,],[197,198,199,201,]),'VALUE':([203,],[207,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'cobol_source_program':([0,],[1,]),'program_id_cobol_source_program':([4,],[5,]),'identification_division_content':([5,30,109,],[7,39,125,]),'empty':([5,25,30,43,44,46,53,57,70,71,77,78,88,109,114,124,129,142,180,208,211,],[9,34,9,48,52,55,63,68,80,83,91,105,113,9,91,80,113,105,34,52,68,]),'enviroment_division_content':([25,180,],[31,190,]),'configuration_section':([25,180,],[32,32,]),'configuration_section_paragrahs':([43,],[45,]),'source_computer_paragraph':([43,],[46,]),'data_division_content':([44,208,],[49,210,]),'object_computer_paragraph':([46,],[53,]),'procedure_division':([49,210,],[57,211,]),'special_names_paragraph':([53,],[61,]),'nested_cobol_source_program':([57,211,],[67,212,]),'data_item_entry':([70,124,],[78,142,]),'stament_declaration_var':([70,78,124,142,],[79,104,79,104,]),'data_file_entry':([71,],[81,]),'paragrahps':([77,114,],[88,129,]),'statements':([77,88,114,129,],[90,112,90,112,]),'stm_display':([77,88,114,129,],[92,92,92,92,]),'stm_acept':([77,88,114,129,],[93,93,93,93,]),'stm_add':([77,88,114,129,],[94,94,94,94,]),'stm_divide':([77,88,114,129,],[95,95,95,95,]),'stm_multiply':([77,88,114,129,],[96,96,96,96,]),'stm_minus':([77,88,114,129,],[97,97,97,97,]),'program_id_nested_cobol_source_program':([86,],[109,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> cobol_source_program","S'",1,None,None,None),
  ('cobol_source_program -> IDENTIFICATION DIVISION PUNTO program_id_cobol_source_program identification_division_content ENVIRONMENT DIVISION PUNTO enviroment_division_content DATA DIVISION PUNTO data_division_content procedure_division nested_cobol_source_program END PROGRAM VARIABLE PUNTO','cobol_source_program',19,'p_cobol_source_program','cobol_parser.py',14),
  ('program_id_cobol_source_program -> PROGRAM_ID PUNTO VARIABLE PUNTO','program_id_cobol_source_program',4,'p_program_id_cobol_source_program','cobol_parser.py',19),
  ('nested_cobol_source_program -> IDENTIFICATION DIVISION PUNTO program_id_nested_cobol_source_program identification_division_content ENVIRONMENT DIVISION PUNTO enviroment_division_content DATA DIVISION PUNTO data_division_content procedure_division nested_cobol_source_program END PROGRAM VARIABLE PUNTO','nested_cobol_source_program',19,'p_nested_cobol_source_program','cobol_parser.py',26),
  ('nested_cobol_source_program -> empty','nested_cobol_source_program',1,'p_nested_cobol_source_program','cobol_parser.py',27),
  ('program_id_nested_cobol_source_program -> PROGRAM_ID PUNTO VARIABLE PUNTO','program_id_nested_cobol_source_program',4,'p_program_id_nested_cobol_source_program','cobol_parser.py',32),
  ('identification_division_content -> AUTHOR PUNTO VARIABLE PUNTO identification_division_content','identification_division_content',5,'p_identification_division_content','cobol_parser.py',38),
  ('identification_division_content -> identification_division_content INSTALLATION PUNTO VARIABLE PUNTO','identification_division_content',5,'p_identification_division_content','cobol_parser.py',39),
  ('identification_division_content -> identification_division_content DATE_WRITTEN PUNTO VARIABLE PUNTO','identification_division_content',5,'p_identification_division_content','cobol_parser.py',40),
  ('identification_division_content -> identification_division_content DATE_COMPILED PUNTO VARIABLE PUNTO','identification_division_content',5,'p_identification_division_content','cobol_parser.py',41),
  ('identification_division_content -> identification_division_content SECURITY PUNTO VARIABLE PUNTO','identification_division_content',5,'p_identification_division_content','cobol_parser.py',42),
  ('identification_division_content -> empty','identification_division_content',1,'p_identification_division_content','cobol_parser.py',43),
  ('enviroment_division_content -> configuration_section','enviroment_division_content',1,'p_enviroment_division_content','cobol_parser.py',49),
  ('configuration_section -> CONFIGURATION SECTION PUNTO','configuration_section',3,'p_configuration_section','cobol_parser.py',54),
  ('configuration_section -> CONFIGURATION SECTION PUNTO configuration_section_paragrahs','configuration_section',4,'p_configuration_section','cobol_parser.py',55),
  ('configuration_section -> empty','configuration_section',1,'p_configuration_section','cobol_parser.py',56),
  ('configuration_section_paragrahs -> source_computer_paragraph object_computer_paragraph special_names_paragraph','configuration_section_paragrahs',3,'p_configuration_section_paragrahs','cobol_parser.py',61),
  ('source_computer_paragraph -> SOURCE_COMPUTER PUNTO VARIABLE PUNTO','source_computer_paragraph',4,'p_source_computer_paragraph','cobol_parser.py',66),
  ('source_computer_paragraph -> empty','source_computer_paragraph',1,'p_source_computer_paragraph','cobol_parser.py',67),
  ('object_computer_paragraph -> OBJECT_COMPUTER PUNTO VARIABLE PUNTO','object_computer_paragraph',4,'p_object_computer_paragraph','cobol_parser.py',72),
  ('object_computer_paragraph -> empty','object_computer_paragraph',1,'p_object_computer_paragraph','cobol_parser.py',73),
  ('special_names_paragraph -> SPECIAL_NAMES PUNTO VARIABLE PUNTO','special_names_paragraph',4,'p_special_names_paragraph','cobol_parser.py',78),
  ('special_names_paragraph -> empty','special_names_paragraph',1,'p_special_names_paragraph','cobol_parser.py',79),
  ('data_division_content -> WORKING_STORAGE SECTION PUNTO data_item_entry','data_division_content',4,'p_data_division_content','cobol_parser.py',91),
  ('data_division_content -> FILE SECTION PUNTO data_file_entry','data_division_content',4,'p_data_division_content','cobol_parser.py',92),
  ('data_division_content -> FILE SECTION PUNTO WORKING_STORAGE SECTION PUNTO data_item_entry','data_division_content',7,'p_data_division_content','cobol_parser.py',93),
  ('data_division_content -> empty','data_division_content',1,'p_data_division_content','cobol_parser.py',94),
  ('data_item_entry -> stament_declaration_var','data_item_entry',1,'p_data_item_entry','cobol_parser.py',99),
  ('data_item_entry -> data_item_entry stament_declaration_var','data_item_entry',2,'p_data_item_entry','cobol_parser.py',100),
  ('data_item_entry -> empty','data_item_entry',1,'p_data_item_entry','cobol_parser.py',101),
  ('data_file_entry -> empty','data_file_entry',1,'p_data_file_entry','cobol_parser.py',106),
  ('stament_declaration_var -> stament_declaration_var NUMERO VARIABLE PIC NUMERO PARENT_IZQ NUMERO PARENT_DER PUNTO','stament_declaration_var',9,'p_stament_declaration_var','cobol_parser.py',111),
  ('stament_declaration_var -> stament_declaration_var NUMERO VARIABLE PIC VARIABLE PARENT_IZQ NUMERO PARENT_DER PUNTO','stament_declaration_var',9,'p_stament_declaration_var','cobol_parser.py',112),
  ('stament_declaration_var -> stament_declaration_var NUMERO VARIABLE PICTURE VARIABLE PARENT_IZQ NUMERO PARENT_DER PUNTO','stament_declaration_var',9,'p_stament_declaration_var','cobol_parser.py',113),
  ('stament_declaration_var -> stament_declaration_var NUMERO VARIABLE PIC VARIABLE PARENT_IZQ NUMERO PARENT_DER PUNTO VALUE STRING','stament_declaration_var',11,'p_stament_declaration_var','cobol_parser.py',114),
  ('stament_declaration_var -> stament_declaration_var NUMERO VARIABLE PIC VARIABLE PUNTO','stament_declaration_var',6,'p_stament_declaration_var','cobol_parser.py',115),
  ('stament_declaration_var -> stament_declaration_var NUMERO VARIABLE PIC NUMERO PUNTO','stament_declaration_var',6,'p_stament_declaration_var','cobol_parser.py',116),
  ('stament_declaration_var -> empty','stament_declaration_var',1,'p_stament_declaration_var','cobol_parser.py',117),
  ('procedure_division -> PROCEDURE DIVISION PUNTO paragrahps','procedure_division',4,'p_procedure_division','cobol_parser.py',122),
  ('procedure_division -> PROCEDURE DIVISION PUNTO MAIN_PROCEDURE PUNTO paragrahps','procedure_division',6,'p_procedure_division','cobol_parser.py',123),
  ('paragrahps -> statements','paragrahps',1,'p_paragrahps','cobol_parser.py',128),
  ('paragrahps -> paragrahps statements','paragrahps',2,'p_paragrahps','cobol_parser.py',129),
  ('paragrahps -> paragrahps statements STOP RUN PUNTO','paragrahps',5,'p_paragrahps','cobol_parser.py',130),
  ('paragrahps -> empty','paragrahps',1,'p_paragrahps','cobol_parser.py',131),
  ('statements -> stm_display','statements',1,'p_statements','cobol_parser.py',136),
  ('statements -> stm_acept','statements',1,'p_statements','cobol_parser.py',137),
  ('statements -> stm_add','statements',1,'p_statements','cobol_parser.py',138),
  ('statements -> stm_divide','statements',1,'p_statements','cobol_parser.py',139),
  ('statements -> stm_multiply','statements',1,'p_statements','cobol_parser.py',140),
  ('statements -> stm_minus','statements',1,'p_statements','cobol_parser.py',141),
  ('statements -> empty','statements',1,'p_statements','cobol_parser.py',142),
  ('stm_display -> DISPLAY STRING PUNTO','stm_display',3,'p_stm_display','cobol_parser.py',147),
  ('stm_display -> DISPLAY STRING VARIABLE PUNTO','stm_display',4,'p_stm_display','cobol_parser.py',148),
  ('stm_display -> stm_display DISPLAY STRING PUNTO','stm_display',4,'p_stm_display','cobol_parser.py',149),
  ('stm_display -> stm_display DISPLAY STRING WITH NO ADVANCING PUNTO','stm_display',7,'p_stm_display','cobol_parser.py',150),
  ('stm_display -> stm_display DISPLAY STRING VARIABLE PUNTO','stm_display',5,'p_stm_display','cobol_parser.py',151),
  ('stm_display -> stm_display DISPLAY VARIABLE STRING PUNTO','stm_display',5,'p_stm_display','cobol_parser.py',152),
  ('stm_display -> stm_display DISPLAY STRING FUNCTION LENGTH PARENT_IZQ VARIABLE PARENT_DER PUNTO','stm_display',9,'p_stm_display','cobol_parser.py',153),
  ('stm_display -> empty','stm_display',1,'p_stm_display','cobol_parser.py',154),
  ('stm_acept -> ACCEPT VARIABLE PUNTO','stm_acept',3,'p_stm_acept','cobol_parser.py',159),
  ('stm_acept -> stm_acept ACCEPT VARIABLE PUNTO','stm_acept',4,'p_stm_acept','cobol_parser.py',160),
  ('stm_acept -> empty','stm_acept',1,'p_stm_acept','cobol_parser.py',161),
  ('stm_add -> ADD VARIABLE TO VARIABLE GIVING VARIABLE PUNTO','stm_add',7,'p_stm_add','cobol_parser.py',166),
  ('stm_add -> ADD VARIABLE TO VARIABLE PUNTO','stm_add',5,'p_stm_add','cobol_parser.py',167),
  ('stm_divide -> DIVIDE VARIABLE INTO VARIABLE GIVING VARIABLE PUNTO','stm_divide',7,'p_stm_divide','cobol_parser.py',172),
  ('stm_divide -> DIVIDE VARIABLE INTO VARIABLE PUNTO','stm_divide',5,'p_stm_divide','cobol_parser.py',173),
  ('stm_multiply -> MULTIPLY VARIABLE BY VARIABLE GIVING VARIABLE PUNTO','stm_multiply',7,'p_stm_multiply','cobol_parser.py',178),
  ('stm_multiply -> MULTIPLY VARIABLE BY VARIABLE PUNTO','stm_multiply',5,'p_stm_multiply','cobol_parser.py',179),
  ('stm_minus -> SUBTRACT VARIABLE FROM VARIABLE GIVING VARIABLE PUNTO','stm_minus',7,'p_stm_minus','cobol_parser.py',184),
  ('stm_minus -> SUBTRACT VARIABLE FROM VARIABLE PUNTO','stm_minus',5,'p_stm_minus','cobol_parser.py',185),
  ('empty -> <empty>','empty',0,'p_empty','cobol_parser.py',191),
]
