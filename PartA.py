class Athlete:
    def __init__(self, name, sex, age, qualifications, records):
        self.name = name
        self.sex = sex
        self.age = age
        self.qualifications = qualifications
        self.records = records

    def print_details(self):
        print("Athlete Details:")
        print(f"Name: {self.name}")
        print(f"Sex: {self.sex}")
        print(f"Age: {self.age}")
        print(f"Qualifications: {self.qualifications}")
        print(f"Records: {self.records}")

    def update_name(self, new_name):
        if isinstance(new_name, str):
            self.name = new_name
        else:
            print("Invalid name. It should be a string.")

    def update_sex(self, new_sex):
        if isinstance(new_sex, str):
            self.sex = new_sex
        else:
            print("Invalid sex.It should be a string.")

    def update_age(self, new_age):
        if isinstance(new_age, int):
            self.sex = new_age
        else:
            print("Invalid sex.It should be an integer.")

    def update_qualifications(self, new_qualifications):
        if isinstance(new_qualifications, list) and all(isinstance (q, str) for q in new_qualifications):
            self.qualifications = new_qualifications
        else:
            print("Invalid qualifications. Should be a list of strings.")

    def update_records(self, new_records):
        if isinstance(new_records, list) and all(isinstance (r, dict) for r in new_records):
            self.records = new_records
        else:
            print("Invalid records. Should be a list of dictionaries.")

class swimmer(Athlete):
    def __init__(self, name, sex, age, qualifications, records, event, personal_best):
        super().__init__(name, sex, age, qualifications, records)
        self.event = event 
        self.personal_best = personal_best
    
    def print_swimmer_details(self):
        super().print_details()
        print(f"Event: {self.event}")
        print(f"Personal Best: {self.personal_best}")

    def update_event(self, new_event):
        if isinstance(new_event, str):
            self.event = new_event
        else:
            print("Invalid event. It should be a string.")

    def update_personal_best(self, new_pb):
        if isinstance(new_pb, str):
            self.personal_best = new_pb
        else:
            print("Invalid personal best. It should be a string.")

athlete1 = Athlete(
    name="John Doe",
    sex="Male",
    age=22,
    qualifications=["World Champion", "European Champion"],
    records=[{"event": "100m backstroke", "time": "56.03s"},{"event": "100m breaststroke", "time": "60.91s"}]
)

swimmer1 = swimmer(
    name="Jane Doe",
    sex="Female",
    age=24,
    qualifications=["Olympian"],
    records=[{"event": "10K marathon swim", "time": "2:10:33.1"}],
    event="10k marathon swim",
    personal_best="2:10:33.1"
)

athlete1.print_details()
print("\n")
swimmer1.print_details()
print("\n")

print("Updating Athlete Atributes...")
athlete1.update_name("Johnathan Doe")
athlete1.update_age(23)
athlete1.print_details()
print("\n")

print("Updating Swimmer Atributes...")
swimmer1.update_event("5K marathon swim")
swimmer1.update_personal_best("1:03:54.32")
swimmer1.print_swimmer_details()
           