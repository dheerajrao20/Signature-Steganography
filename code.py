import os


dir_path = r'.//media//images//'

# list to store files


def img_names(dir_path):
    res = []
    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            res.append(path)
    return res

res=img_names(dir_path)

for i in range(0, len(res)):
    os.remove(dir_path + res[i])

res.clear()

res=img_names(dir_path)

print(res)