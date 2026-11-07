class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        heappush = heapq.heappush
        heappop = heapq.heappop
        heapreplace = heapq.heapreplace
        heapify = heapq.heapify
        
        SHIFT = 18
        MASK = (1 << SHIFT) - 1
        
        # Precompute packed representations: (weight << 18) | index
        server_packed = [(w << SHIFT) | i for i, w in enumerate(servers)]
        
        idle = server_packed[:]
        heapify(idle)
        busy = []  # stores: (free_time << 18) | server_index
        
        m = len(tasks)
        ans = [0] * m
        cur_time = 0
        
        for j, t in enumerate(tasks):
            if cur_time < j:
                cur_time = j
                
            # If no idle servers, fast-forward to earliest completion
            if not idle:
                cur_time = busy[0] >> SHIFT
                cur_limit = (cur_time << SHIFT) | MASK
                
                # Check root's children (index 1 and 2) to see if more than one server finishes at cur_time
                n_busy = len(busy)
                multi = False
                if n_busy > 1 and busy[1] <= cur_limit:
                    multi = True
                elif n_busy > 2 and busy[2] <= cur_limit:
                    multi = True
                
                # SAFE HEAPREPLACE: Only 1 server finishes at cur_time
                if not multi:
                    s_idx = busy[0] & MASK
                    ans[j] = s_idx
                    heapreplace(busy, ((cur_time + t) << SHIFT) | s_idx)
                    continue

            # Standard path: multiple servers finished, or idle was not empty
            cur_limit = (cur_time << SHIFT) | MASK
            while busy and busy[0] <= cur_limit:
                idx = heappop(busy) & MASK
                heappush(idle, server_packed[idx])
                
            best = heappop(idle)
            s_idx = best & MASK
            ans[j] = s_idx
            heappush(busy, ((cur_time + t) << SHIFT) | s_idx)
            
        return ans
