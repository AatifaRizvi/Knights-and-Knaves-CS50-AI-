from logic import *

# Define symbols
AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")


# Puzzle 0
# A says: "I am both a knight and a knave."
knowledge0 = And(
    # A is either a knight or a knave, but not both
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    # If A is a knight, his statement is true
    Implication(AKnight, And(AKnight, AKnave)),

    # If A is a knave, his statement is false
    Implication(AKnave, Not(And(AKnight, AKnave)))
)


# Puzzle 1
# A says: "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),

    # If A is a knight, his statement is true
    Implication(AKnight, And(AKnave, BKnave)),

    # If A is a knave, his statement is false
    Implication(AKnave, Not(And(AKnave, BKnave)))
)


# Puzzle 2
# A says: "We are the same kind."
# B says: "We are of different kinds."
knowledge2 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),

    # A’s statement: “We are the same kind.”
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),

    # B’s statement: “We are of different kinds.”
    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),
    Implication(BKnave, Not(Or(And(AKnight, BKnave), And(AKnave, BKnight))))
)


# Puzzle 3
# A says either "I am a knight" or "I am a knave", but we don't know which.
# B says: "A said 'I am a knave'." and "C is a knave."
# C says: "A is a knight."
knowledge3 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),

    # A’s possible statements (unknown which he said)
    # We represent the uncertainty using an Or condition:
    # (Either A said "I am a Knight" or A said "I am a Knave")
    # If A said "I am a Knight" → statement = AKnight
    # If A said "I am a Knave" → statement = AKnave
    # We can treat this as A’s possible self-reference.

    # B says: "A said 'I am a Knave'." and "C is a Knave."
    # So B's whole statement means: A said "I am a Knave" AND CKnave is true.
    Implication(BKnight, And(AKnave, CKnave)),
    Implication(BKnave, Not(And(AKnave, CKnave))),

    # C says: "A is a Knight."
    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnight))
)


# List of puzzles
puzzles = [
    ("Puzzle 0", knowledge0),
    ("Puzzle 1", knowledge1),
    ("Puzzle 2", knowledge2),
    ("Puzzle 3", knowledge3)
]


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    for (name, knowledge) in puzzles:
        print(name)
        for symbol in symbols:
            if model_check(knowledge, symbol):
                print(f"    {symbol}")


if __name__ == "__main__":
    main()
