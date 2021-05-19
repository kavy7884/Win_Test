# Basic dictionary
contact = {"kavy": "0961104567", "anna": "0985697314", "jane": "7997979979"}
print(contact)

# get/modified contents
print(contact["kavy"])
contact["jane"] = 899889989
print(contact["jane"])

# add contents
contact["david"] = 7997979979
print(contact)

# delete contents
del contact["jane"]
print(contact)

# pop data
print(contact.pop("david"))
print(contact.pop("david", "Does not exist!"))
print(contact.popitem())

# clear/delete data
contact.clear()
print(contact)
del contact

contact = {"kavy": "0961104567", "anna": "0985697314"}
print(contact)

# shallow/deep copy data
contact_1 = contact.copy()
contact["ggg"] = "77887788"
print(contact)
print(contact_1)

contact_2 = contact
contact_2["yyy"] = "99999"

print(contact)
print(contact_1)
print(contact_2)

# length
print(len(contact))
print(len(contact_1))
print(len(contact_2))

# update
new_contact = {}
new_contact.update(contact)
new_contact.update(contact_1)
new_contact.update(contact_2)
print(new_contact)

# check exist
if "kavy" in new_contact:
    print("kavy exist!")
else:
    print("kavy does not exist!")

# new dictionary by tuple/list and zip
data = [("ttt", "1234567"), ("zzz", "8888888")]
dict_data = dict(data)
print(dict_data)
new_contact.update(dict_data)
print(new_contact)

zip_data = zip(("uuu", "rrr"), ("4444", "66666"))
dict_zip_data = dict(zip_data)
print(dict_zip_data)
new_contact.update(dict_zip_data)
print(new_contact)

# loop dictionary (key, value)
for name, phone in new_contact.items():
    print(name, phone)

# loop dictionary (keys)
for name in new_contact.keys():
    print(name)

for name in new_contact:
    print(name)

# loop dictionary (values)
for phone in new_contact.values():
    print(phone)

# sort dictionary by values
sorted_contact_by_phone = sorted(new_contact.items(), key=lambda item:item[1])
print(sorted_contact_by_phone)

# create dictionary by keys
keys_1 = ["Taiwan", "Japan"]
new_dict_1 = dict.fromkeys(keys_1)
print(new_dict_1)
new_dict_2 = dict.fromkeys(keys_1, "GOGOGO")
print(new_dict_2)

# get/setdefault values
print(new_dict_2.get("Taiwan"))
print(new_dict_2.get("China", "Fuck"))
print(new_dict_2.setdefault("Taiwan", "Taipei"))
del new_dict_2["Taiwan"]
print(new_dict_2.setdefault("Taiwan", "Taipei"))

# new dictionary by generator
word = "deeplearning"
alphabet_count = {alphabet:word.count(alphabet) for alphabet in word}
print(alphabet_count)
