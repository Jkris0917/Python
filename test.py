students = {
    "ace": {
        "score": 90,
        "grades": 90,
        "passed": True,
    },
    "bob": {
        "score": 80,
        "grades": 80,
        "passed": True,
    },
    "cindy": {
        "score": 50,
        "grades": 60,
        "passed": False,
    }
}

for name, info in students.items():
    print(f"\n{name.title()}")
    for field,value in info.items():
        print(f'{field}: {value}')