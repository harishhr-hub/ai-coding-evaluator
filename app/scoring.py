def final_score(corr, eff, read, mod, edge):
    total = (
        corr * 0.35 +
        eff * 0.20 +
        read * 0.15 +
        mod * 0.15 +
        edge * 0.15
    )
    return int(total)
