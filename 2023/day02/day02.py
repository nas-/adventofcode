from pathlib import Path
from dataclasses import dataclass

inputs = (Path(__file__).parent / "input").read_text()

@dataclass
class Game:
    blue: int = 0
    red: int = 0
    green: int = 0

    @classmethod
    def from_game_string(cls, game_str):
        splitted = [x.split() for x in game_str.split(",")]
        x = {i[1]: int(i[0]) for i in splitted}
        return cls(**x)

    def possible(self, other: "Game"):
        return (
            self.blue <= other.blue
            and self.green <= other.green
            and self.red <= other.red
        )


bagcontents = Game(blue=14, red=12, green=13)

cleaned = [i.split(":") for i in inputs.splitlines()]
res = {}

for x in cleaned:
    game_id = int(x[0].split(" ")[1])
    games = [Game.from_game_string(u) for u in x[1].split(";")]
    res[game_id] = games

result_part_1 = sum(
    [x for x, y in res.items() if all(k.possible(bagcontents) for k in y)]
)
print(f"{result_part_1= }")

result_part_2 = 0
for i, x in res.items():
    result_part_2 += (
        max(i.red for i in x) * max(i.blue for i in x) * max(i.green for i in x)
    )

print(f"{result_part_2= }")
