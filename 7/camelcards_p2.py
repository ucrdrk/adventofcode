#!/usr/bin/env python3

import re
import sys

from functools import cmp_to_key

hand_re = re.compile(r'^[2-9AKQJT]+')
joker_re = re.compile(r'(J+)\s*$')

sorted_cards = 'AKQT98765432J'

five_of_a_kind_re = re.compile(r'([2-9AKQT])\1{4}')
four_of_a_kind_re = re.compile(r'([2-9AKQT])\1{3}')
full_house_re = re.compile(r'((([2-9AKQT])\3)([2-9AKQT])\4{2})|((([2-9AKQT])\7{2})([2-9AKQT])\8)')
three_of_a_kind_re = re.compile(r'([2-9AKQT])\1{2}')
two_pair_re = re.compile(r'([2-9AKQT])\1.*([2-9AKQT])\2')
pair_re = re.compile(r'([2-9AKQT])\1')

ranks = [pair_re, two_pair_re, three_of_a_kind_re, full_house_re, four_of_a_kind_re, five_of_a_kind_re]
joker_upgrades = [{'J': 1, 'JJ': 3, 'JJJ': 5, 'JJJJ': 6, 'JJJJJ': 6}, 
                  {'J': 3, 'JJ': 5, 'JJJ': 6}, 
                  {'J': 4}, 
                  {'J': 5, 'JJ': 6},
                  {}, 
                  {'J': 6},
                  {}]

def card_cmp(card1, card2):
    return sorted_cards.index(card1) - sorted_cards.index(card2)

class Hand:
    def __init__(self, cards, bid):
        self.orig = cards
        self.sorted =  ''.join(sorted(cards, key=cmp_to_key(card_cmp)))
        self.bid = bid
        self.rank = self.determine_rank()

    def __repr__(self):
        return f"<cards: [{self.orig} -> {self.sorted}], rank: {self.rank}, bid: {self.bid}>\n"
    
    def __lt__(self, other):
        if self.rank != other.rank:
            return self.rank < other.rank
        idx = 0
        while(self.orig[idx] == other.orig[idx]):
            idx += 1
        return sorted_cards.index(self.orig[idx]) > sorted_cards.index(other.orig[idx])
    
    def determine_rank(self):
        rank = 0
        for rank_idx in range(len(ranks)-1,-1, -1):
            match = ranks[rank_idx].search(self.sorted)
            if match != None:
                rank = rank_idx + 1
                break

        match = joker_re.search(self.sorted)
        if match != None and bool(joker_upgrades[rank]):
            rank = joker_upgrades[rank][match.group(1)]
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
print(hands)
sum = 0
for idx in range(0, len(hands)):
    sum += (idx + 1) * hands[idx].bid
print(sum)