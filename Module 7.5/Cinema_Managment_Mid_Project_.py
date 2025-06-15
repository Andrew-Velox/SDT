class Star_Cinema:

    hall_list=[]

    def entry_hall(self, hall):
        self.hall_list.append(hall)
    
class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.seats={}
        self.show_list=[]
        self.rows=rows
        self.cols=cols
        self.hall_no=hall_no
    
    def entry_show(self,id,movie_name,time):
        self.show_list.append((id, movie_name, time))

        seats=[]

        for _ in range(self.rows):
            seats.append([0]*self.cols)
        self.seats[id] = seats

    def book_seats(self,id,list_of_row_col):
        if id not in self.seats:
            print("Show not found")
            return
        
        for seat in list_of_row_col:
            row,col=seat
            if row<0 or row>=self.rows or col<0 or col>=self.cols:
                print(f"Invalid seat: ({row}, {col})")
            elif self.seats[id][row][col]==1:
                print(f"Seat ({row}, {col}) is already booked")
            else:
                self.seats[id][row][col]=1
                print(f"Seat ({row}, {col}) booked successfully")

    def view_show_list(self):
        for show in self.show_list:
            print(f"ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")


    def view_available_seats(self,id):
        if id not in self.seats:
            print("Show not found")
            return
        
        for row in self.seats[id]:
            print(row)

        

    # def __str__(self):
    #     return f"rows: {self.rows}, cols: {self.cols}, hall_no: {self.hall_no}, seats: {self.seats}, show_list: {self.show_list}"

        

hall_1 = Hall(10, 10, "A")
hall_1.entry_show(1, "Avengers", "10:00 AM")
hall_1.entry_show(2, "Batman", "12:00 PM")
hall_1.entry_show(3, "Superman", "02:00 PM")

print(hall_1)

while 1:
    print("\n")
    print("1. View Show List")
    print("2. View Available Seats")
    print("3. Book Seats")
    print("4. Exit")
    print("\n")
    opt = int(input("Enter your choice: "))
    print("\n")


    if opt == 1:
        hall_1.view_show_list()
    elif opt == 2:
        show_id = int(input("Enter show ID: "))
        hall_1.view_available_seats(show_id)
    elif opt == 3:
        show_id = int(input("Enter show ID: "))
        row = int(input("Enter row number: "))
        col = int(input("Enter column number: "))
        hall_1.book_seats(show_id,[(row,col)])
    elif opt == 4:
        print("Exiting...")
        break
    else:
        print("Invalid option, please try again.")

