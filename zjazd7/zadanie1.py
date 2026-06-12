from collections import Counter


class Theatre:
    def __init__(self, *number_of_seats_per_row):
        self.seats = []
        for e in number_of_seats_per_row:
            self.seats.append([0] * e)

    def display(self):
        max_len = len(max(self.seats, key=len))
        for r_index, row in enumerate(self.seats):
            prefix = f"{r_index + 1}: "
            content = "".join([f"{(s_index + 1):^3}" if seat == 0 else f"{'x':^3}" for s_index, seat in enumerate(row)])
            print(f"{prefix} {content:^{max_len * 3}}")

    def buy_ticket(self, row, seat, seat_to = -1):
        seat -= 1
        row -= 1
        if seat_to == -1:
            seat_to = seat + 1

        for i in range(seat, seat_to):
            self.seats[row][i] = 1

    def show_free(self, row = -1):
        rows_to_check = [row - 1] if row != -1 else range(len(self.seats))
        for r_index in rows_to_check:
            free_seats = [s_index + 1 for s_index, seat in enumerate(self.seats[r_index]) if seat == 0]
            print(f"Row {r_index + 1}, free seats: {free_seats if free_seats else 'No free seats'}")

    def show_summary(self, ticket_cost):
        flat_seats = sum(self.seats, [])
        dic = Counter(flat_seats)
        sold = dic[1]
        total = dic[0] + sold
        print(f"Ticket sold: {sold}/{total}, Income: {ticket_cost * sold}")

th = Theatre(4, 8, 10, 10)
th.display()
th.buy_ticket(1, 4)
th.buy_ticket(4, 1, 6)
th.buy_ticket(4, 10)
th.buy_ticket(2, 1, 8)
th.buy_ticket(3, 5, 10)
th.display()
th.show_free()
th.show_free(4)
th.show_summary(5)