class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        to_ret = []
        my_dict = {}

        for s in strs: 
            sorted_s = str(sorted(s))
            if sorted_s in my_dict:
                my_dict[sorted_s].append(s)
            else:
                my_dict[sorted_s] = [s]     

        return list(my_dict.values())