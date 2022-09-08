class Solution:
    def firstBadVersion(self, n: int, left=0) -> int:
        # set version to be checked to center version of all versions
        version = left + int((n-left)/2)
        
        # end conditions
        if version == left:
            if isBadVersion(left) == True:
                return left
            return n
        
        # if the checked version is not bad, continue search after excluding 
        # older half of versions by incrementing left marker "left"
        if isBadVersion(version) == False:
            return self.firstBadVersion(n, version)
        # else, if checked version is bad, continue search after excluding 
        # newer half of versions by incrementing right marker "n"
        return self.firstBadVersion(version, left)
