def value_cards(cards):
    res, aces = 0, 0
    for c in cards:
        if c.isdigit(): res += int(c)
        elif c in 'JQK': res += 10
        else: aces += 1
    res += aces
    for _ in range(aces):
        if res + 10 <= 21: res += 10
    return res

bank=input().split()
player=input().split()
bc=value_cards(bank)
hc=value_cards(player)
bank_blackjack=len(bank)==2 and bc==21
player_blackjack=len(player)==2 and hc==21
if player_blackjack and not bank_blackjack: print("Blackjack!")
elif bank_blackjack and not player_blackjack: print("Bank")
elif hc>21 and bc>21: print("Bank")
elif hc>21: print("Bank")
elif bc>21: print("Player")
elif hc>bc: print("Player")
elif bc>hc: print("Bank")
else: print("Draw")
