class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        frequency = {}
 
        left = 0
        max_fruits = 0
 
        # Expand the window by adding each fruit from the right.
        for right in range(len(fruits)):
            fruit = fruits[right]
 
            frequency[fruit] = (
                frequency.get(fruit, 0) + 1
            )
 
            # Remove one left fruit when more than two types are present.
            if len(frequency) > 2:
                left_fruit = fruits[left]
                frequency[left_fruit] -= 1
 
                # Remove a type after its final fruit leaves the window.
                if frequency[left_fruit] == 0:
                    del frequency[left_fruit]
 
                left += 1
 
            # Only valid windows can contribute to the final answer.
            if len(frequency) <= 2:
                max_fruits = max(
                    max_fruits,
                    right - left + 1
                )
 
        return max_fruits
        