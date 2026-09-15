def main():
    b = int(input())
    new_titles = [input() for _ in range(b)]
    unique_new = list(dict.fromkeys(new_titles))

    N = int(input())
    shelf = []
    for _ in range(N):
        line = input()
        name, rank = line.rsplit(' ', 1)
        rank = None if rank == "None" else int(rank)
        shelf.append((name, rank))

    original_ranks = [r for t, r in shelf if r is not None]
    fav_rank = max(original_ranks) if original_ranks else None

    new_set = set(unique_new)
    remaining_shelf = [(t, r) for t, r in shelf if t not in new_set]
    d = N - len(remaining_shelf)
    u = len(unique_new)
    needed = max(0, u - d)

    ranks_present = sorted(set(r for t, r in remaining_shelf if r is not None))
    removable_ranks = [r for r in ranks_present if r != fav_rank]

    groups_removed = set()
    removed_count = 0
    for r in removable_ranks:
        if removed_count >= needed:
            break
        count_r = sum(1 for t, rk in remaining_shelf if rk == r)
        groups_removed.add(r)
        removed_count += count_r

    if removed_count < needed:
        print("Your TBR is out of control Clara!")
        return

    final_titles = [t for t, r in remaining_shelf if r not in groups_removed] + unique_new
    final_titles.sort(key=lambda x: x.lower())

    for t in final_titles:
        print(t)

if __name__ == "__main__":
    main()