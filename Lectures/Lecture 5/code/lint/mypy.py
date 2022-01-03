# Case 1
def boo(x: int) -> int:
    return x + 1


def foo(x: int) -> float:
    return x + 2

boo(foo('a'))


# Case 2
def append_1(x: list[int]) -> list:
    return x + [1]


def add_a_key(x: dict[int,str]) -> dict[int,str]:
    return {**x, **{1: 'a'}}


append_1((1,2,3))
add_a_key({1,2,3})