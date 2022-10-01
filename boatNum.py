class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
    
        boat, le,rig = 0, 0, len(people) - 1
        people.sort()
        while le <= rig:
            if people[le] + people[rig] <= limit:
                le += 1
                rig -= 1
            else:
                rig -= 1
            boat += 1
        return boat
    