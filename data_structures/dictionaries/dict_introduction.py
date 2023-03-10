empty_dict = dict()
print(empty_dict)

phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbuster": 44678
              }

print(phone_book)
print(phone_book.values())
print(phone_book.keys())
print(phone_book["Batman"])
print(phone_book.get("Ghostbuster"))

# add new entries
phone_book["Mimi"] = 112233
phone_book["Meomeo"] = 445566
phone_book["Ghostbuster"] = 12345
print(phone_book)

del phone_book["Batman"]
print(phone_book)

cersei = phone_book.pop("Cersei")
print(phone_book)
print(cersei)
print(len(phone_book))
print("Mimi" in phone_book)
print("Batman" in phone_book)

another_phone_book = {"Catwoman": 67423, "Jamie": 237734, "Godzilla": 98776}
used_phone_book = {}
used_phone_book.update(another_phone_book)
phone_book.update(another_phone_book)
print(phone_book)
print(used_phone_book)

houses = {1: "Gryffindor", 2: "Slytherin", 3: "Hufflepuff", 4: "Ravenclaw"}
new_houses = {n**2: house + "!" for (n, house) in houses.items()}
print(new_houses)