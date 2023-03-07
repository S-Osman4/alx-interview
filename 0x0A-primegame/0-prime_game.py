#!/usr/bin/python3
"""
Module: Game of choosing Prime numbers
"""


def is_prime(n):
    """
    Check if a number is prime or not
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def isWinner(x, nums):
    """
    Determine the winner of the game
    """
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        primes = [i for i in range(2, n+1) if is_prime(i)]
        maria_turn = True
        while primes:
            if maria_turn:
                # Maria's turn
                selected_prime = primes.pop(0)
                # Remove selected prime and its multiples from the list
                primes = [i for i in primes if i % selected_prime != 0]
                maria_turn = False
            else:
                # Ben's turn
                selected_prime = primes.pop(0)
                # Remove selected prime and its multiples from the list
                primes = [i for i in primes if i % selected_prime != 0]
                maria_turn = True
        # Update the number of rounds won by each player
        if maria_turn:
            ben_wins += 1
        else:
            maria_wins += 1
    # Determine the player with the most wins
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
