def replace(s, old, new):
    split_list = s.split(old)

    changed_list = new

    changed_list = changed_list.join(split_list)
    return changed_list

s = "I love spom! Spom is my favorite food. Spom, spom, spom, yum!"

print(replace(s, "love", "hate"))