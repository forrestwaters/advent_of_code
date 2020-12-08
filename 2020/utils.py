def read_input(fn: str) -> "list[str]":
    with open(fn, "r") as f:
        return [x.rstrip("\n") for x in f.readlines()]
