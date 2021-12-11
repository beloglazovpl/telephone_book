import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

# TODO 1: выполните пункты 1-3 ДЗ
def check(data):
  if " " in data[0]:
    name = data[0].split(" ")
    if len(name) == 3:
      lastname = name[0]
      firstname = name[1]
      surname = name[2]
    if len(name) == 2:
      lastname = name[0]
      firstname = name[1]
      surname = data[2]
  if " " not in data[0]:
    lastname = data[0]
    if " " in data[1]:
      name = data[1].split(" ")
      firstname = name[0]
      surname = name[1]
    if " " not in data[1]:
      firstname = data[1]
      surname = data[2]
  organization = data[3]
  position = data[4]
  phone = data[5]
  pattern = r"(\+7|8)+\s*[\(]*(\d{3})[\)]*[-\s]*(\d{3})[-\s]*(\d{2})[-\s]*(\d{2})(\s*)[\(]*([\доб.]*)\s*([\d]*)[\)]*"
  res = re.sub(pattern, r"+7(\2)\3-\4-\5\6\7\8", phone)
  phone_new = res
  email = data[6]
  new_employee = [lastname, firstname, surname, organization, position, phone_new, email]
  return new_employee

# приводим адресную книгу к единообразию, телефонные номера записываем в одном стиле
update_contacts_list_ = []
for i in range(len(contacts_list)):
  update_contacts_list_.append(check(contacts_list[i]))

# убираем повторения из адресной книги
dic = {}
for rec in update_contacts_list_:
  if dic.get(rec[0]+rec[1]) is not None:
    new_list_ = []
    for i in range(len(rec)):
      if len(rec[i]) >= len(dic[rec[0]+rec[1]][i]):
        new_list_.append(rec[i])
      else:
        new_list_.append(dic[rec[0]+rec[1]][i])
    dic[rec[0]+rec[1]] = new_list_
  else:
    dic[rec[0]+rec[1]] = rec

# приобразовываем адресную книгу в списки
final_contact_list = []
for key, value in dic.items():
  final_contact_list.append(value)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(final_contact_list)
