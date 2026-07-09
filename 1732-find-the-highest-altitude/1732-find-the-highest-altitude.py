class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_altitude = 0
        current_altitude = 0
        
        for g in gain:
            current_altitude += g  # Calculate the cumulative running sum
            if current_altitude > max_altitude:
                max_altitude = current_altitude
                
        return max_altitude

#The Concept (Prefix Sum): You start at altitude 0. You are given an array gain representing net altitude changes. You need to find the highest peak you ever hit.
#Strategy: Maintain a running total (current_altitude) and a tracker for the highest value that running total ever reached (max_altitude).

#Time Complexity: $O(N)$ to iterate through the gains.Space Complexity: $O(1)$ since we only store two integers.
