import collections

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        
        # Create two queues to store the indices of senators from each party.
        radiant_queue = collections.deque()
        dire_queue = collections.deque()

        for i, party in enumerate(senate):
            if party == 'R':
                radiant_queue.append(i)
            else:
                dire_queue.append(i)

        # Continue the process as long as both parties have senators.
        while radiant_queue and dire_queue:
            # Get the index of the next senator from each party.
            r_index = radiant_queue.popleft()
            d_index = dire_queue.popleft()

            # The senator with the smaller index gets to vote and ban the other.
            # The winner is added back to the end of their queue for the next round.
            # We add 'n' to their index to signify they are in the next round.
            if r_index < d_index:
                radiant_queue.append(r_index + n)
            else:
                dire_queue.append(d_index + n)
        
        # The party with senators remaining in its queue is the winner.
        return "Radiant" if radiant_queue else "Dire"

    '''
## Complexity Analysis \U0001f4ca
Time Complexity: O(N). Although we're in a while loop, in each step, one senator is permanently eliminated. The total number of banning operations cannot exceed N, making the process linear.

Space Complexity: O(N). In the beginning, the two queues together store all N initial indices of the senators.
    '''