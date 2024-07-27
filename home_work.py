class Telefon:

    def __init__(self, number=''):
        self.number = number
        self.incoming_calls = 0

    def set_number(self, number):
        self.number = number
        print(number)

    def get_incoming_calls(self):
        return self.incoming_calls
    
    def calls(self):
        self.incoming_calls += 1
    
        

phone1 = Telefon()
phone2 = Telefon()
phone3 = Telefon()

phone1.set_number('723-973-148')
phone2.set_number('222-333-444')
phone3.set_number('111-111-111')

for _ in range(5):
    phone1.calls()

for _ in range(8):
    phone2.calls()

for _ in range(9):
    phone3.calls()

def total_incoming_calls(phones):
    total_calls = 0
    for phone in phones:
        total_calls += phone.get_incoming_calls()
    return total_calls
    
phones = [phone1, phone2, phone3]

total_calls = total_incoming_calls(phones)
print("Osszes hivas: " , total_calls)






        