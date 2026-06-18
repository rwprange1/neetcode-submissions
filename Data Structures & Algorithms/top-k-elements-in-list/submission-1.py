class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        my_dict = {}
        for num in nums:
            if num in my_dict:
                my_dict[num] = my_dict[num] + 1
            else: 
                my_dict[num] = 1    

        items = my_dict.items()
        sorted_items = sorted(items, key=lambda count:count[1])

        return list(map(lambda i: i[0], sorted_items[-k:]))
                  