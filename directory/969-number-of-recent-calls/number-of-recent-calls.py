import collections

class RecentCounter:
    """
    A class to count recent requests within a 3000ms time frame.
    """
    def __init__(self):
        """
        Initializes the counter with an empty queue to store request timestamps.
        """
        self.requests = collections.deque()

    def ping(self, t: int) -> int:
        """
        Adds a new request at time 't' and returns the number of requests
        in the inclusive range [t - 3000, t].
        """
        # Step 1: Add the new request's timestamp to the queue.
        self.requests.append(t)
        
        # Step 2: Remove any timestamps from the front of the queue that are
        # now too old (i.e., less than t - 3000).
        while self.requests[0] < t - 3000:
            self.requests.popleft()
            
        # Step 3: The remaining size of the queue is the answer.
        return len(self.requests)


# Example of how the class is used:
# obj = RecentCounter()
# print(obj.ping(1))      # Output: 1
# print(obj.ping(100))    # Output: 2
# print(obj.ping(3001))   # Output: 3

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)