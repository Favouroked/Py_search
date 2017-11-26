import os
total_hits = []
def search(the_dir, name):
    files_in_dir = os.listdir(the_dir)
    for i in files_in_dir:
        if name in i:
            total_hits.append(os.path.join(the_dir, i))
        if os.path.isdir(os.path.join(the_dir, i)):
            search(os.path.join(the_dir, i), name)

search('/home/favour/FAv', 'oluwa')
print(total_hits)
