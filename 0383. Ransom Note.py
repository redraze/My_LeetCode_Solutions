class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        noteDict, magazineDict = {}, {}

        for ch in ransomNote:
            noteDict[ch] = noteDict.get(ch, 0) + 1

        for ch in magazine:
            if magazineDict.get(ch, 0) < noteDict.get(ch, 0):
                magazineDict[ch] = magazineDict.get(ch, 0) + 1
            if magazineDict == noteDict:
                return True
        
        return False
