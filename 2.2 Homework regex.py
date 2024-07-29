import re
import csv
from pprint import pprint


regex = r"(\+7|8)\s*?[\s-]*\(?(\d{3})\)?[\s-]*(\d{3})?[\s-]*(\d{2})?[\s-]*(\d{2})?[\s]*?[\s]*\(?(\w+.)?[\s]*?(\d+)\)?"
with open('phonebook_raw.csv', 'r', encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
db = contacts_list
for value in range(len(db)):
    data_name = ' '.join(db[value][:3]).split()
    if len(data_name) == 1:
        data_name.insert(1, '')
        data_name.insert(2, '')
    elif len(data_name) == 2:
        data_name.insert(2, '')
    del db[value][:3]

    for ind, v in enumerate(data_name):
        db[value].insert(ind, v)
    text = ' '.join(db[value])

for i in range(len(db)):
    for j in range(len(db[i])):
        subst = "+7(\\2)\\3-\\4-\\5 \\6\\7"
        #result = re.sub(regex, subst, text, 0)
        result = re.sub(regex, subst, db[i][j], 0)
        if result:
            if len(result) > 15 and result[14] == ' ':
                result = result.replace(' ', '')
            db[i][j] = result
#pprint(db)

from collections import OrderedDict


def remove_duplicates(list_: list) -> list:
    k = 0
    while k < len(list_) - 1:
        for list1, list2 in zip(list_[k], list_[k + 1]):
            #print(list1, list2)
            if list1 == list2:
                new_list = list(OrderedDict.fromkeys(list_[k] + list_[k + 1]))
                #print(new_list)
                list_.remove(list_[k + 1])
                list_.remove(list_[k])
                list_.append(new_list)
            break
        k += 1
    return list_


unique_data_list = remove_duplicates(db)
#print(unique_data_list)
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Р’РјРµСЃС‚Рѕ contacts_list РїРѕРґСЃС‚Р°РІСЊС‚Рµ СЃРІРѕР№ СЃРїРёСЃРѕРє
  datawriter.writerows(unique_data_list)
