#!/usr/bin/env python3

import re
import sys

from functools import cmp_to_key

hand_re = re.compile(r'^[2-9AKQJT]+')

sorted_cards = 'AKQJT98765432'

five_of_a_kind_re = re.compile(r'([2-9AKQJT])\1{4}')
four_of_a_kind_re = re.compile(r'([2-9AKQJT])\1{3}')
full_house_re = re.compile(r'((([2-9AKQJT])\3)([2-9AKQJT])\4{2})|((([2-9AKQJT])\7{2})([2-9AKQJT])\8)')
three_of_a_kind_re = re.compile(r'([2-9AKQJT])\1{2}')
two_pair_re = re.compile(r'([2-9AKQJT])\1.*([2-9AKQJT])\2')
pair_re = re.compile(r'([2-9AKQJT])\1')

ranks = [pair_re, two_pair_re, three_of_a_kind_re, full_house_re, four_of_a_kind_re, five_of_a_kind_re]

def card_cmp(card1, card2):
    return sorted_cards.index(card1) - sorted_cards.index(card2)

class Hand:
    def __init__(self, cards, bid):
        self.orig = cards
        self.sorted =  ''.join(sorted(cards, key=cmp_to_key(card_cmp)))
        self.bid = bid
        self.rank = self.determine_rank()

    def __repr__(self):
        return f"<cards: {self.orig}, rank: {self.rank}, bid: {self.bid}>"
    
    def __lt__(self, other):
        if self.rank != other.rank:
            return self.rank < other.rank
        idx = 0
        while(self.orig[idx] == other.orig[idx]):
            idx += 1
        return sorted_cards.index(self.orig[idx]) > sorted_cards.index(other.orig[idx]
        )
    def determine_rank(self):
        rank = 0
        for rank_idx in range(len(ranks)-1,-1, -1):
            match = ranks[rank_idx].search(self.sorted)
            if match != None:
                rank = rank_idx + 1
                break
        return rank

bid_re = re.compile(r'\d+\s*$')
hands = []
for line in sys.stdin.readlines():
    match = hand_re.search(line)
    if match == None:
        continue

    bid = int(bid_re.search(line).group(0))
    hand = Hand(match.group(0), bid)
    hands.append(hand)

hands = sorted(hands)

sum = 0
for idx in range(0, len(hands)):
    sum += (idx + 1) * hands[idx].bid
print(sum)