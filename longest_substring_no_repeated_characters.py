class Solution(object):
    biggest = 0

    def lengthOfLongestSubstring(self, s):
        sol = Solution()
        index = 0
        j = 0
        lst = list(s)
        trailing = []
        hold = []
        for x in lst:
            # print(lst.index(x))
            # print("index",index)
            # print("x",x)
            trailing.append(x)
            # print("hold",hold)
            if x in hold:
                if sol.biggest < len(hold):
                    sol.biggest = len(hold)
                temp = hold.index(x)
                j = len(trailing) - 1 - len(hold) + temp
                # print("j",j)
                # print("temp:", temp, "length of Trailing:", len(trailing), "len(hold)", len(hold), "j:", j)
                index += 1
                hold = list(lst[j + 1:index])
                # print("hold",hold)

            else:
                hold.append(x)
                index += 1
                if len(hold) > sol.biggest:
                    sol.biggest = len(hold)
        return sol.biggest


solution_obj = Solution()
a = solution_obj.lengthOfLongestSubstring("au")
print(a)
