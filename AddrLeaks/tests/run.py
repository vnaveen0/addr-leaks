#!/usr/bin/python

import os
import subprocess

from termcolor import colored


files = ['direct1.bc', 'direct2.bc', 'direct3.bc', 'direct4.bc', 'direct5.bc',
         'indirect1.bc', 'indirect2.bc', 'indirect3.bc', 'indirect4.bc',
         'array1.bc', 'array2.bc', 'array3.bc', 'array4.bc',
         'struct1.bc', 'struct2.bc', 'struct3.bc',
         'context1.bc',
         'inter1.bc', 'inter2.bc',
         'strings1.bc', 'strings2.bc', 'strings3.bc', 'strings4.bc',
         'list1.bc', 'list2.bc',
         'flow1.bc', 'flow2.bc', 'flow3.bc'
         ]

print '#### Regression tests ###\n'
template = "{0:20}|{1:20}"
print template.format("FILE", "RESULT")

for filename in files:
    _file = open(filename, 'rb')
    p = subprocess.Popen(['opt', '-load', '../../../../Release/lib/AddrLeaks.so',
                          '-mem2reg', '-instnamer', '-internalize', '-inline', 
                          '-globaldce', '-addrleaks'],
                         shell=False, stdin=_file, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    result = p.communicate()[1]

    passed = True

    if filename == 'direct1.bc':
        if result.find('File: direct1.c, Line: 9') == -1: passed = False
    elif filename == 'direct2.bc':
        if result.find('File: direct2.c, Line: 9') == -1: passed = False
    elif filename == 'direct3.bc':
        if result.find('File: direct3.c, Line: 10') == -1: passed = False
    elif filename == 'direct4.bc':
        if result.find('File: direct4.c, Line: 11') == -1: passed = False
    elif filename == 'direct5.bc':
        if result.find('File: direct5.c, Line: 14') == -1: passed = False
        if result.find('File: direct5.c, Line: 13') == -1: passed = False
    elif filename == 'indirect1.bc':
        if result.find('File: indirect1.c, Line: 10') == -1: passed = False
        if result.find('File: indirect1.c, Line: 14') == -1: passed = False
    elif filename == 'indirect2.bc':
        if result.find('File: indirect2.c, Line: 17') != -1: passed = False
        if result.find('File: indirect2.c, Line: 18') != -1: passed = False
        if result.find('File: indirect2.c, Line: 19') != -1: passed = False
        if result.find('File: indirect2.c, Line: 20') != -1: passed = False
        if result.find('File: indirect2.c, Line: 24') == -1: passed = False
        if result.find('File: indirect2.c, Line: 25') == -1: passed = False
        if result.find('File: indirect2.c, Line: 26') == -1: passed = False
        if result.find('File: indirect2.c, Line: 27') == -1: passed = False
    elif filename == 'indirect3.bc':
        if result.find('File: indirect3.c, Line: 13') == -1: passed = False
        if result.find('File: indirect3.c, Line: 14') == -1: passed = False
        if result.find('File: indirect3.c, Line: 15') == -1: passed = False
    elif filename == 'indirect4.bc':
        if result.find('File: indirect4.c, Line: 12') != -1: passed = False
        if result.find('File: indirect4.c, Line: 13') != -1: passed = False
    elif filename == 'array1.bc':
        if result.find('File: array1.c, Line: 10') == -1: passed = False
        if result.find('File: array1.c, Line: 11') != -1: passed = False
        if result.find('File: array1.c, Line: 12') != -1: passed = False
        if result.find('File: array1.c, Line: 13') != -1: passed = False
        if result.find('File: array1.c, Line: 14') != -1: passed = False
        if result.find('File: array1.c, Line: 15') != -1: passed = False
        if result.find('File: array1.c, Line: 19') == -1: passed = False
        if result.find('File: array1.c, Line: 20') != -1: passed = False
        if result.find('File: array1.c, Line: 21') != -1: passed = False
        if result.find('File: array1.c, Line: 22') != -1: passed = False
        if result.find('File: array1.c, Line: 23') == -1: passed = False
        if result.find('File: array1.c, Line: 24') != -1: passed = False
    elif filename == 'array2.bc':
        if result.find('File: array2.c, Line: 12') != -1: passed = False
        if result.find('File: array2.c, Line: 16') == -1: passed = False
        if result.find('File: array2.c, Line: 17') == -1: passed = False
        if result.find('File: array2.c, Line: 18') == -1: passed = False
        if result.find('File: array2.c, Line: 19') == -1: passed = False
        if result.find('File: array2.c, Line: 20') == -1: passed = False
        if result.find('File: array2.c, Line: 21') == -1: passed = False
    elif filename == 'array3.bc':
        if result.find('File: array3.c, Line: 15') != -1: passed = False
        if result.find('File: array3.c, Line: 17') == -1: passed = False
    elif filename == 'array4.bc':
        if result.find('File: array4.c, Line: 17') != -1: passed = False
        if result.find('File: array4.c, Line: 20') == -1: passed = False
    elif filename == 'struct1.bc':
        if result.find('File: struct1.c, Line: 19') == -1: passed = False
        if result.find('File: struct1.c, Line: 20') != -1: passed = False
        if result.find('File: struct1.c, Line: 21') == -1: passed = False
    elif filename == 'struct2.bc':
        if result.find('File: struct2.c, Line: 25') == -1: passed = False
        if result.find('File: struct2.c, Line: 26') != -1: passed = False
        if result.find('File: struct2.c, Line: 27') == -1: passed = False
        if result.find('File: struct2.c, Line: 28') == -1: passed = False
    elif filename == 'struct3.bc':
        if result.find('File: struct3.c, Line: 21') != -1: passed = False
        if result.find('File: struct3.c, Line: 22') == -1: passed = False
    elif filename == 'context1.bc':
        passed = True
    elif filename == 'inter1.bc':
        if result.find('File: inter1.c, Line: 16') == -1: passed = False
    elif filename == 'inter2.bc':
        if result.find('File: inter2.c, Line: 27') == -1: passed = False
        if result.find('File: inter2.c, Line: 28') == -1: passed = False
        if result.find('File: inter2.c, Line: 29') == -1: passed = False
        if result.find('File: inter2.c, Line: 30') == -1: passed = False
    elif filename == 'strings1.bc':
        if result.find('File: strings1.c, Line: 12') == -1: passed = False
        if result.find('File: strings1.c, Line: 15') == -1: passed = False
    elif filename == 'strings2.bc':
        if result.find('File: strings2.c, Line: 11') == -1: passed = False
    elif filename == 'strings3.bc':
        if result.find('File: strings3.c, Line: 11') != -1: passed = False
    elif filename == 'strings4.bc':
        if result.find('File: strings4.c, Line: 10') != -1: passed = False
    elif filename == 'list1.bc':
        if result.find('File: list1.c, Line: 35') == -1: passed = False
    elif filename == 'list2.bc':
        if result.find('File: list2.c, Line: 32') != -1: passed = False
    elif filename == 'flow1.bc':
        if result.find('File: flow1.c, Line: 10') != -1: passed = False
        if result.find('File: flow1.c, Line: 14') == -1: passed = False
    elif filename == 'flow2.bc':
        if result.find('File: flow2.c, Line: 9') != -1: passed = False
        if result.find('File: flow2.c, Line: 13') == -1: passed = False
    elif filename == 'flow3.bc':
        if result.find('File: flow3.c, Line: 9') != -1: passed = False
        if result.find('File: flow3.c, Line: 13') == -1: passed = False

    if passed:
        print template.format(filename, colored('\tPASSED', 'green'))
    else:
        print template.format(filename, colored('\tFAILED', 'red'))


