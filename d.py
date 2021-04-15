import random

student_dict = {'Eric': 80, 'Scott': 75, 'Jessa': 95, 'Mike': 66}
print("Dictionary Before Shuffling")
print(student_dict)
keys = list(student_dict.keys())
random.shuffle(keys)

ShuffledStudentDict = dict()
for key in keys:
    ShuffledStudentDict.update({key: student_dict[key]})

print("\nDictionary after Shuffling")
print(ShuffledStudentDict)