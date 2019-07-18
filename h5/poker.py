import random


def open_new_poker():
    flower = ['♠黑桃', '♦方塊', '♣梅花', '♥愛心']
    number = ['１', '２', '３', '４', '５', '６', '７', '８', '９', '１０', 'Ｊ', 'Ｑ', 'Ｋ']
    cards = []
    for i in flower:
        for j in number:
            cards.append(str(i) + str(j))
    return cards


def licensing1(cards):
    card_table = []
    player = []
    print(cards)
    for i in range(1, 1000):
        card = cards.pop(random.randint(0, 51))
        cards.insert(random.randint(0, 51), card)
    print(cards)
    for i in range(0, 13):
        for j in range(0, 4):
            if i == 0:
                card_table.append([])
                card_table[j].append(cards.pop())
            else:
                card_table[j].append(cards.pop())

    print(card_table[0], '\n', card_table[1], '\n', card_table[2], '\n', card_table[3])


def licensing2(cards):
    card_table = []
    player = []
    print(cards)
    for i in range(1, 1000):
        card = cards.pop(random.randint(0, 51))
        cards.insert(random.randint(0, 51), card)
    print(cards)
    for i in range(1, 5):
        for j in range(1, 14):
            player.append(cards.pop(0))
        card_table.append(player)
        player = []

    print(card_table[0], '\n', card_table[1], '\n', card_table[2], '\n', card_table[3])


def main():
    new_poker = open_new_poker()
    # licensing2(new_poker)
    licensing1(new_poker)


main()
