students = [
    {"id": 1, "name": "Nguyen Van A"},
    {"id": 2, "name": "Tran Thi B"}
]

def search_students(query):
    query = query.lower()
    return [s for s in students if query in s["name"].lower()]

if __name__ == "__main__":
    print(search_students("Nguyen"))
