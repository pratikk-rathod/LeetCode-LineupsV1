class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        n = len(original)
        adj_dic = dict()
        head_dic = collections.defaultdict(list)
        for i in range(n):
            if ((original[i],changed[i]) in adj_dic):
                adj_dic[(original[i],changed[i])]= min(adj_dic[(original[i],changed[i])], cost[i])
            else:
                adj_dic[(original[i],changed[i])]= cost[i]
                head_dic[original[i]].append(changed[i])
        
        #print("head_dic", head_dic)
        #print("adj_dic", adj_dic)
        @cache
        def minCost(node1, node2) -> int:

            pq = [(0, node1)]
            cost_for_node = collections.defaultdict(lambda:math.inf)
            cost_for_node[node1] = 0
            while pq:
                curr_cost, curr_node = heappop(pq)
                if curr_cost > cost_for_node[curr_node]:
                    continue
                if curr_node == node2:
                    return curr_cost
                
                ls = head_dic[curr_node]
                for neighbor in ls:
                    cost = adj_dic[(curr_node, neighbor)]
                    new_cost = curr_cost + cost
                    if new_cost < cost_for_node[neighbor]:
                        cost_for_node[neighbor] = new_cost
                        heappush(pq, (new_cost, neighbor))
            return -1
    
        m = len(source)
        ans = 0
        for i in range(m):
            if source[i] != target[i]:
                t= minCost(source[i], target[i])
                #print(source[i], target[i], t)
                if t == -1:
                    return -1
                ans += t
        
        return ans