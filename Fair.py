class Ticket:
    def __init__(self, ticket_type, quantity):
        self.ticket_type = ticket_type
        self.quantity = quantity

    def calculate_price(self):
        if self.ticket_type == "adult":
            return self.quantity * 100
        elif self.ticket_type == "child":
            return self.quantity * 50
        elif self.ticket_type == "elder":
            return self.quantity * 75
        else:
            return 0

class EventTicket(Ticket):
    def __init__(self, ticket_type, quantity, event_name):
        super().__init__(ticket_type, quantity)
        self.event_name = event_name

    def calculate_price(self):
        base_price = super().calculate_price()
        if self.event_name == "magic_show":
            return base_price * 1.2  # 20% surcharge for event1
        elif self.event_name == "music_night":
            return base_price * 1.5  # 50% surcharge for event2
        elif self.event_name == "classical_dance":
            return base_price * 2.0  # 100% surcharge for event3
        else:
            return base_price

class BookingSystem:
    def __init__(self):
        self.tickets = []

    def add_ticket(self, ticket):
        self.tickets.append(ticket)

    def calculate_total_price(self):
        total_price = 0
        for ticket in self.tickets:
            total_price += ticket.calculate_price()
        return total_price

    def display_tickets(self):
        for ticket in self.tickets:
            print(f"{ticket.quantity} {ticket.ticket_type} ticket(s) for {ticket.event_name}")

booking_system = BookingSystem()


while True:
    print(" WELCOME to The Heritage Fest ")
    ticket_type = input("Enter ticket type (adult/child/elder): ")
    if ticket_type not in ["adult", "child", "elder"]:
        print("Invalid ticket type")
        continue
    quantity = int(input("Enter quantity: "))
    if quantity <= 0:
        print("Invalid quantity")
        continue
    event_name = input("Enter event name (magic_show/music_night/classical_dance): ")
    if event_name not in ["magic_show", "music_night", "classical_dance"]:
        print("Invalid event name")
        continue
    ticket = EventTicket(ticket_type, quantity, event_name)
    booking_system.add_ticket(ticket)
    if input("Add more tickets? (y/n): ") != "y":
        break

booking_system.display_tickets()
print("Total price:", booking_system.calculate_total_price())
print("Thank You! Enjoy The Heritage Fest")
