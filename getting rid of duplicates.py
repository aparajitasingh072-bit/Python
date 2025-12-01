student_data = {'idl' : {'name': ['Sara'], 'class': ['V'], 'subject_intergration': ['english, math, science'] }, 

'id2': {'name': ['David'], 'class': ['V'], 'subject_intergration': ['english, math, science'] },

'id3': {'name': ['Sara'], 'class': ['V'], 'subject_intergration': ['english, math, science'] }, 

'id4': {'name': ['Surya'], 'class': ['V'], 'subject_intergration': ['english, math, science'] }} 

Result = {}

for key, value in student_data.items():
    if value not in Result.values():
        Result[key] = value

print(Result)