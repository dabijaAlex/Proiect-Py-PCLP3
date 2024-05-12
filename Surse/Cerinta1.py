#!/usr/bin/env python3

def has_duplicate_lines():
    with open("train.csv", 'r') as file:
        lines = file.readlines()
        unique_lines = set(lines)
    return len(unique_lines) != len(lines)


def format_line(line):
    line = line.strip('\n')
    list_of_line = line.split(',')
    merged_elem = list_of_line[3] + "," + list_of_line[4]
    list_of_line[3:5] = [merged_elem]
    return list_of_line
    pass

def check_type(element):

    tip = "string"

    try:
        float(element)
        tip = "float"
    except ValueError:
        pass

    try:
        int(element)
        tip = "int"
    except ValueError:
        pass

    return tip

def get_types_for_each(list_of_line, tipuri_pt_col):
    for i in range(len(list_of_line)):
        if list_of_line[i] != '':
            type_of_data = check_type(list_of_line[i])
            tipuri_pt_col[cols[i]] = type_of_data
    return tipuri_pt_col

def count_nr_elems_each_col(list_of_line, nr_elem_pe_col):
    for i in range(len(list_of_line)):
        if list_of_line[i] != '':
            nr_elem_pe_col[i] += 1
    return nr_elem_pe_col

f = open('train.csv', 'r')

#numaram coloaneale
line = f.readline()
line = line.strip('\n')

cols = line.split(',')
nr_coloane = len(cols)
print("nr coloane = ", nr_coloane)


tipuri_pt_col = {}
for i in cols:
    tipuri_pt_col[i] = "default"

nr_lines = 0
nr_elem_lipsa_pe_col = [0] * 12
line = f.readline()

while line:
    nr_lines += 1
    list_of_line = format_line(line)
    tipuri_pt_col = get_types_for_each(list_of_line, tipuri_pt_col)

    nr_elem_lipsa_pe_col = count_nr_elems_each_col(list_of_line, nr_elem_lipsa_pe_col)

    line = f.readline()

print(tipuri_pt_col)

for i in range(len(nr_elem_lipsa_pe_col)):
    nr_elem_lipsa_pe_col[i] = nr_lines - nr_elem_lipsa_pe_col[i]
print(nr_elem_lipsa_pe_col)

print("nr linii = ", nr_lines)

print("Does the file have dupes ?", has_duplicate_lines())
f.close()

