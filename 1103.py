class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> list[int]:
        curr_candy = 1
        arr = [0] * num_people

        while candies > curr_candy:  # distribute 1, 2, 3, ... candies
            person = curr_candy % num_people - 1
            arr[person] += curr_candy
            candies -= curr_candy
            curr_candy += 1

        arr[person + 1] += candies # distribute last candies
        return arr