lst = [
    ('a', 14), ('b', 17), ('a', 15), ('b', 7),
    ('c', 16), ('e', 10), ('f', 14), ('e', 17),
    ('a', 13), ('c', 19), ('d', 15), ('b', 18),
    ('d', 11), ('a', 12), ('d', 10), ('d', 10)
]

def best_three(name_score_list):
    best_scores = {}
    curr_leaders = []
    for name, score in name_score_list:
        if name not in best_scores or best_scores[name] < score:
            best_scores[name] = score

        new_leaders = sorted(best_scores.items(), key=lambda item: item[1], reverse=True)[:3]
        if new_leaders != curr_leaders:
            curr_leaders = new_leaders
            if len(new_leaders) == 3:
                print(f"leaders changed: {new_leaders}")

    return curr_leaders

print(best_three(lst))