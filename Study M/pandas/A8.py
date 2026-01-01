class Train:
    def __init__(self, train_id, name, source, destination, seats, price):
        self.train_id = train_id
        self.name = name
        self.source = source
        self.destination = destination
        self.seats = seats
        self.price = price  # Price per ticket

class RailwayManagementSystem:
    def __init__(self):
        self.trains = []

    def add_train(self, train):
        self.trains.append(train)

    def find_train(self, train_id):
        for train in self.trains:
            if train.train_id == train_id:
                return train
        return None

    def display_trains(self):
        print("Train ID\tName\tSource\tDestination\tAvailable Seats\tPrice per Ticket")
        for train in self.trains:
            print(f"{train.train_id}\t\t{train.name}\t{train.source}\t{train.destination}\t\t{train.seats}\t\t{train.price}")

    def book_ticket(self, train_id, num_tickets, customer_name):
        train = self.find_train(train_id)
        if train:
            if train.seats >= num_tickets:
                total_price = num_tickets * train.price
                train.seats -= num_tickets
                print(f"Booking successful for {num_tickets} tickets on train {train.name}. Total price: ${total_price}")
                self.write_to_file(customer_name, train, num_tickets, total_price)
            else:
                print("Sorry, not enough seats available for booking.")
        else:
            print("Train not found.")

    def write_to_file(self, customer_name, train, num_tickets, total_price):
        filename = f"{customer_name}_booked_tickets.txt"
        with open(filename, "a") as file:
            file.write(f"Train Name: {train.name}\n, Source: {train.source}\n, Destination: {train.destination}\n, "
                       f"Number of Tickets: {num_tickets}\n, Total Price: ${total_price}\n")

    def cancel_ticket(self, train_id, num_tickets):
        train = self.find_train(train_id)
        if train:
            train.seats += num_tickets
            total_refund = num_tickets * train.price
            print(f"{num_tickets} tickets canceled for train {train.name}. Refund amount: ${total_refund}")
        else:
            print("Train not found.")

def main():
    railway_system = RailwayManagementSystem()

    # Adding some trains with prices
    railway_system.add_train(Train(1, "Express", "City A", "City B", 100, 50))
    railway_system.add_train(Train(2, "Fast", "City B", "City C", 50, 40))
    railway_system.add_train(Train(3, "Local", "City C", "City D", 200, 30))

    customer_name = input("Enter your name: ")

    while True:
        print("\nWelcome to Railway Management System")
        print("1. Display Available Trains")
        print("2. Book Ticket")
        print("3. Cancel Ticket")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            railway_system.display_trains()
        elif choice == "2":
            train_id = int(input("Enter train ID: "))
            num_tickets = int(input("Enter number of tickets: "))
            railway_system.book_ticket(train_id, num_tickets, customer_name)
        elif choice == "3":
            train_id = int(input("Enter train ID: "))
            num_tickets = int(input("Enter number of tickets to cancel: "))
            railway_system.cancel_ticket(train_id, num_tickets)
        elif choice == "4":
            print("Thank you for using Railway Management System!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()