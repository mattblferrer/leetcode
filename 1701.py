class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        waiting_time = 0
        current_time = customers[0][0]  # get time first customer arrives

        for c in customers:
            arrive_time, order_time = c[0], c[1]  # unpack customer data
            if arrive_time > current_time:  # customer arrived while chef idle
                current_time = arrive_time
            elif arrive_time < current_time:  # customer arrived while past order
                waiting_time += current_time - arrive_time  
            waiting_time += order_time
            current_time += order_time

        return waiting_time / len(customers)  # get average of all waiting times

