class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        n = len(nums)
        first_pref = [float('inf')] * k
        first_pref[0] = -1
        
        distinct_v_list = [0]
        min_i_for_virtual = [float('inf')] * k
        next_v_to_process = [0] * k
        
        ans = 0
        curr_pref = 0
        
        for j in range(n):
            curr_pref = (curr_pref + nums[j]) % k
            d = (2 * nums[j]) % k
            
            idx = next_v_to_process[d]
            while idx < len(distinct_v_list):
                v = distinct_v_list[idx]
                r = (v + d) % k
                if first_pref[v] < min_i_for_virtual[r]:
                    min_i_for_virtual[r] = first_pref[v]
                idx += 1
            next_v_to_process[d] = idx
            
        
            if first_pref[curr_pref] != float('inf'):
                ans = max(ans, j - first_pref[curr_pref])
            
            if min_i_for_virtual[curr_pref] != float('inf'):
                ans = max(ans, j - min_i_for_virtual[curr_pref])
                
            
            if first_pref[curr_pref] == float('inf'):
                first_pref[curr_pref] = j
                distinct_v_list.append(curr_pref)
                
        return ans