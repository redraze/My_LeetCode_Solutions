class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # frequency dictionary of all characters in s1
        # linear runtime
        freq = {}
        for ch in s1:
            try:
                freq[ch] += 1
            except KeyError:
                freq[ch] = 1
                
        # check to make sure each character in s1 
        # exists in s2 in enough quantity
        temp = {}
        for ch in s2:
            try:
                temp[ch] += 1
            except KeyError:
                temp[ch] = 1
        for key, value in freq.items():
            try:
                if value > temp[key]:
                    return False
            except KeyError:
                return False
        
        # so many loops and conditional statements...
        i = 0
        while i < len(s2):
            if s2[i] in freq:
                temp = dict(freq)
                j = i
                while j < len(s2):
                    ch = s2[j]
                    # ch not in temp
                    if ch not in temp:
                        if ch not in freq:
                            i = j
                            break
                        while ch not in temp and i < j:
                            if s2[i] == ch:
                                i += 1
                                j += 1
                                break
                            if s2[i] in temp:
                                temp[s2[i]] += 1
                            else:
                                temp[s2[i]] = 1
                            i += 1
                        continue
                    # ch in temp                     
                    if temp[ch] == 1:
                        temp.pop(ch)
                    else:
                        temp[ch] -= 1
                    j += 1
                    if temp == {}:
                        return True
            i += 1
        return False
