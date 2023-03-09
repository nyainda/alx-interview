#!/usr/bin/python3

def isWinner(x, nums):
    """
    Determines the winner of a game of prime numbers.

    Args:
        x (int): The number of rounds to play.
        nums (list): A list of integers representing the end of the set
            of consecutive integers for each round.

    Returns:
        str: The name of the player that won the most rounds. If the
            winner cannot be determined, returns None.
    """
    def is_prime(n):
        """Returns True if n is prime, False otherwise."""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Helper function for determining the winner of a round
    def round_winner(n):
        maria_moves = 0
        while n > 0:
            # Maria picks the smallest prime number in the set
            for i in range(2, n+1):
                if is_prime(i):
                    n -= i
                    maria_moves += 1
                    break
            else:
                # If no primes left, Ben wins
                return 'Ben'
            
            # Ben picks the largest prime number in the remaining set
            for i in range(n, 1, -1):
                if is_prime(i):
                    n -= i
                    break
        
        # If no numbers left, Maria wins
        return 'Maria'

    # Play each round and determine the winner
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        winner = round_winner(n)
        if winner == 'Maria':
            maria_wins += 1
        elif winner == 'Ben':
            ben_wins += 1
    
    # Determine overall winner
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
