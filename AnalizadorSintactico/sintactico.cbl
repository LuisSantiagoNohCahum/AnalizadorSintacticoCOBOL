IDENTIFICATION DIVISION.
PROGRAM-ID. USODEACCEPT.
AUTHOR. HIRONAKAMURA.
INSTALLATION. GITHUB.

**********************************************************
* COBCALC                                                *
*                                                        *
* Un programa simple que permite realizar funciones      *
* financieras utilizando funciones intrinsecas.          *
*                                                        *
**********************************************************

ENVIRONMENT DIVISION.
CONFIGURATION SECTION.
SOURCE-COMPUTER. HP.
OBJECT-COMPUTER. HP.


DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-NOMBRE PIC A(34.7).
01 WS-NUMERO PIC 9(3).

