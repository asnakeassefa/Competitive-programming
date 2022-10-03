class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        start = 0
        end = 0
        max_length = 0
        fruit = {}
        while end < len(fruits):
            fruit[fruits[end]] = end
            
            if len(fruit) >= 3:
                least = min(fruit.values())
                del fruit[fruits[least]]
                start = least + 1
            max_length = max(max_length,end-start+1)
            end += 1
        return max_length