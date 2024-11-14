def checking_for_perfection():
    st = [[i, "not two o"] for i in input().split()]
    for word in st:
        if (
            word[0].count("о") == 2 or word[0].count("o") == 2
        ):  # Проверка русской и английской о
            word[1] = "two o"

    if len(st) % 2 != 1:
        if not any("not two o" in sp for sp in st):
            return "Идеально"
    return "Думай ещё"

print(checking_for_perfection())
