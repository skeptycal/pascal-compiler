# -*- scanner.py -*-
# -*- MIT License (c) 2014 David Leonard -*-
# -*- drksephy.github.io -*-

#################
#     TODO      #
#################

# - [done] Scan <target program>
# - [    ] Tokenize keywords

import sys

def scan(source):
    # Reads <source program> and builds tokens. 

    # Variables to assist with tokenization
    # row/col of current character
    curr_row = 1
    curr_col = 1
    # Current value of token
    curr_val = 0
    # Curent token
    curr_token = 0

    text = open(source, 'r').read().splitlines()
    for line in text:
        curr_col = 1
        for char in line: 
                    
            # Treat all ascii chars <= 32 as spaces
            if to_ascii(char) == 32:
                print "row: " + str(curr_row) + " , " + "col: " + str(curr_col) + " is: " + char
            # Check if char: ! " # $ % & ' ( ) * + , - . / : ; < = > ? @

            if ((to_ascii(char) > 32 and to_ascii(char) < 47) or (to_ascii(char) > 57 and to_ascii(char) < 65)):
                print "row: " + str(curr_row) + " , " + "col: " + str(curr_col) + " is: " + char

            # Check if char: 0 1 2 3 4 5 6 7 8 9
            if to_ascii(char) > 47 and to_ascii(char) < 58:
                print "row: " + str(curr_row) + " , " + "col: " + str(curr_col) + " is: " + char
            # Check if char is uppercase

            if to_ascii(char) > 64 and to_ascii(char) < 91:
                print "row: " + str(curr_row) + " , " + "col: " + str(curr_col) + " is: " + char 
            # Check if char is lowercase

            if to_ascii(char) > 96 and to_ascii(char) < 123:
                print "row: " + str(curr_row) + " , " + "col: " + str(curr_col) + " is: " + char

            # Check if char: [ \ ] ^ _ `
            if to_ascii(char) > 90 and to_ascii(char) < 97:
                print "row: " + str(curr_row) + " , " + "col: " + str(curr_col) + " is: " + char

            # Check if char: { | } ~ DEL
            if to_ascii(char) > 122 and to_ascii(char) < 128:
                print "row: " + str(curr_row) + " , " + "col: " + str(curr_col) + " is: " + char
            curr_col += 1
        curr_row += 1


def lookup(table, key):
    # Reads token value from corresponding table
    return table[key]

def to_ascii(char):
    # Returns ascii value of a character
    return ord(char)


KEYWORDS = {
    'BEGIN'     : 'TK_BEGIN',
    'BREAK'     : 'TK_BREAK',
    'CONST'     : 'TK_CONST',
    'DO'        : 'TK_DO',
    'DOWNTO'    : 'TK_DOWNTO',
    'ELSE'      : 'TK_ELSE',
    'END'       : 'TK_END',
    'FOR'       : 'TK_FOR',
    'FUNCTION'  : 'TK_FUNCTION',
    'IF'        : 'TK_IF',
    'LABEL'     : 'TK_LABEL', 
    'PROGRAM'   : 'TK_PROGRAM',
    'REPEAT'    : 'TK_REPEAT',
    'STRING'    : 'TK_STRING', 
    'THEN'      : 'TK_THEN',
    'TO'        : 'TK_TO',
    'TYPE'      : 'TK_TYPE',
    'VAR'       : 'TK_VAR',
    'WHILE'     : 'TK_WHILE'
}

OPERATORS = {
    '+'         : 'TK_PLUS',
    '-'         : 'TK_MINUS',
    '*'         : 'TK_MULT',
    '/'         : 'TK_DIV_FLOAT',
    'DIV'       : 'TK_DIV',
    'MOD'       : 'TK_MOD',
    ':'         : 'TK_COLON',
    '='         : 'TK_EQUALS',
    '>'         : 'TK_GREATER',
    '<'         : 'TK_LESS',
    '>='        : 'TK_GREATER_EQUALS',
    '<='        : 'TK_LESS_EQUALS',
    'AND'       : 'TK_AND',
    'OR'        : 'TK_OR',
    'NOT'       : 'TK_NOT'
}