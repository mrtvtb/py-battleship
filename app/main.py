class Deck:
    def __init__(self, row: int, column: int, is_alive: bool = True) -> None:
        self.row = row
        self.column = column
        self.is_alive = is_alive


class Ship:
    def __init__(
            self,
            start: tuple,
            end: tuple,
            is_drowned: bool = False) -> None:
        self.is_drowned = is_drowned
        self.decks = []
        if start[0] == end[0]:
            for i in range(start[1], end[1] + 1):
                self.decks.append(Deck(start[0], i))
        else:
            for i in range(start[0], end[0] + 1):
                self.decks.append(Deck(i, end[1]))

    def get_deck(self, row: int, column: int) -> Deck:
        for deck in self.decks:
            if deck.row == row and deck.column == column:
                return deck

    def fire(self, row: int, column: int) -> str:
        deck = self.get_deck(row, column)

        if deck is None:
            return "Miss!"

        deck.is_alive = False

        if all(not deck.is_alive for deck in self.decks):
            self.is_drowned = True
            return "Sunk!"

        return "Hit!"


class Battleship:
    def __init__(self, ships: list[tuple]) -> None:
        self.field = {}
        for ship in ships:
            self.field[ship] = Ship(ship[0], ship[1])

    def fire(self, location: tuple) -> str:
        for ship in self.field.values():
            deck = ship.get_deck(location[0], location[1])
            if deck is not None:
                return ship.fire(location[0], location[1])
        return "Miss!"
