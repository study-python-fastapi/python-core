List = {"name":"Ronaldo","age":35,"sport":"football","high":195}
for key, value in List.items():
    print(f"{key} is {value}")

Books = {"1984":1949,"To Kill a Mockingbird":1960,"The Catcher in the Rye":1951}
print(Books)
Book = {"Harry Potter":2007}
Books.update(Book)
print(Books)

Countryes_capitals = {"Ukraine": "Kyiv", "USA": "Washington", "German": "Berlin"}
country = str(input("Enter Country: "))
check = Countryes_capitals.keys()
if country in check:
    print(Countryes_capitals.get(country))
else:
    print("Country not in list")