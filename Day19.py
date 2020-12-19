import re

rules, messages = open("input19.txt").read().split("\n\n")


def maketree(rules):
    tree = {}
    for line in rules.splitlines():
        left, right = line.split(": ")
        if right.startswith('"'):
            tree[int(left)] = eval(right)
        else:
            tree[int(left)] = [[*map(int, part.split())] for part in (right.split(" | "))]
    return tree


tree = maketree(rules)


def build(idx):
    rule = tree[idx]
    if isinstance(rule, str):
        return rule
    if len(rule) == 1:
        return "".join(map(build, rule[0]))
    return "(?:" + "|".join("".join(map(build, r)) for r in rule) + ")"


compiled = re.compile("^" + build(0) + "$")
print(sum(map(bool, map(compiled.match, messages.splitlines()))))

extra_rules = """
8: 42 | 42 8
11: 42 31 | 42 11 31
"""

tree = maketree(rules + extra_rules)

aha = re.compile(f"^(?:{build(42)})+?(?:" \
                 + "|".join(f"(?:{build(42)}){{{n}}}(?:{build(31)}){{{n}}}" for n in range(1, 10)) \
                 + ")$")
print(sum(map(bool, map(aha.match, messages.splitlines()))))
