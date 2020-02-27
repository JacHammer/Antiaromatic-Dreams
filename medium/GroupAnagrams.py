# Minci
# time elapsed: 54 min
# submitted 1 time


from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        d_list = []
        for word in strs:
            word_dict = dict()
            for i in range(len(word)):
                if word[i] in word_dict:
                    word_dict[word[i]] += 1
                else:
                    word_dict[word[i]] = 1
            if d_list == []:
                d_list.append([word_dict, word])
                continue
            else:
                for i in d_list:
                    if word_dict == i[0]:
                        i.append(word)
                        break
                else:
                    d_list.append([word_dict, word])
        for i in d_list:
            output.append(i[1:len(i)])
        return output


sol = Solution()
ans = sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(ans)
