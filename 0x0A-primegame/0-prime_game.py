#!/usr/bin/python3
"""
This represents a prime game with two contestant, the first one without prime numbers loses.
"""


def isWinner(x, nums):
    """ 
    Detects the winner in the Prime Game
    """
    if x <= 0 or not nums:
        return None

    n = max(nums)
    deck = [True for x in range(max(n + 1, 2))]
    for i in range(2, int(pow(n, 0.5)) + 1):
        if not deck[i]:
            continue
        for j in range(i*i, n + 1, i):
            deck[j] = False

    deck[0] = deck[1] = False
    c = 0
    for i in range(len(deck)):
        if deck[i]:
            c += 1
        deck[i] = c

    player1 = 0
    for n in nums:
        player1 += deck[n] % 2 == 1
    if player1 * 2 > len(nums):
        return "Maria"
    if player1 * 2 == len(nums):
        return None
    return "Ben" n > 0:
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

rn None
