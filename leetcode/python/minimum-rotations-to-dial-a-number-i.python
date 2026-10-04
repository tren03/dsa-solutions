class Solution:
    def minRotations(self, s: str) -> int:
        # from cur, you can go to dest in 2 ways
        # for each step - return the min way
        ans = 0
        cur = 0
        prev = -1

        while cur < len(s):
            # if both are same, no dials needed

            prev_val = None
            if prev == -1:
                prev_val = 0
            else:
                prev_val = int(s[prev])

            if prev_val == int(s[cur]):
                prev = cur
                cur += 1
                #print("way is 0 when both eq")
                continue
            

                
            # prev and cur are diff
            way_1 = abs(int(prev_val)-int(s[cur]))
            
            if int(prev_val) > int(s[cur]):
                mx = prev_val
                mn = s[cur]
            else:
                mx = s[cur]
                mn = prev_val
            t = int(mx)
            c = 0
            while t != int(mn):
                c+=1
                t+=1
                t=t%10
            ans += min(c, way_1)
            prev = cur
            cur += 1
            #print("way1", way_1)
            #print("way2", c)
            #print("chosen", min(way_1, c))
            
        

        return ans
            

