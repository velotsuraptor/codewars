def cakes(recipe, available):
    numb = {}
    for i in recipe.keys():
        if i not in available.keys():
            return 0
    for k2, v2 in recipe.items():
        for k1, v1 in available.items():
            if k1 == k2:
                numb[k2] = v1//v2
    return min(numb.values())