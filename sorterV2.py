import os

main_path = str(__file__)
py_name = main_path.split("/")[-1]
py_name = "/" + py_name
main_path = main_path.replace(py_name, "")

text_path = main_path + "/locations.txt"


#### Functions ####
def pics(download, pic):
    src = []
    dst = str(pic)
    if dst[-1] != "/":
        dst += "/"
    else:
        dst = str(pic)

    start_point = r"{}".format(download)

    for root, dirs, files in os.walk(start_point):
        for file in files:
            if file.endswith(".jpg"):
                src.append(os.path.join(root, file))
            if file.endswith(".png"):
                src.append(os.path.join(root, file))

    for location in src:
        file_name = location.split("/")[-1]
        os.rename(location, dst + file_name)


def videos(download, vid):
    src = []
    dst = str(vid)
    if dst[-1] != "/":
        dst += "/"
    else:
        dst = str(vid)

    start_point = r"{}".format(download)

    for root, dirs, files in os.walk(start_point):
        for file in files:
            if file.endswith(".mp4"):
                src.append(os.path.join(root, file))
            if file.endswith(".mkv"):
                src.append(os.path.join(root, file))

    for location in src:
        file_name = location.split("/")[-1]
        os.rename(location, dst + file_name)


def document(download, documents):
    src = []
    dst = str(documents)
    if dst[-1] != "/":
        dst += "/"
    else:
        dst = str(documents)

    start_point = r"{}".format(download)

    for root, dirs, files in os.walk(start_point):
        for file in files:
            if file.endswith(".pdf"):
                src.append(os.path.join(root, file))

    for location in src:
        file_name = location.split("/")[-1]
        os.rename(location, dst + file_name)


def zip(download, zips):
    src = []
    dst = str(zips)
    if dst[-1] != "/":
        dst += "/"
    else:
        dst = str(zips)

    start_point = r"{}".format(download)

    for root, dirs, files in os.walk(start_point):
        for file in files:
            if file.endswith(".zip"):
                src.append(os.path.join(root, file))
            if file.endswith(".rar"):
                src.append(os.path.join(root, file))

    for location in src:
        file_name = location.split("/")[-1]
        os.rename(location, dst + file_name)


def music(download, musics):
    src = []
    dst = str(musics)
    if dst[-1] != "/":
        dst += "/"
    else:
        dst = str(musics)

    start_point = r"{}".format(download)

    for root, dirs, files in os.walk(start_point):
        for file in files:
            if file.endswith(".mp3"):
                src.append(os.path.join(root, file))
            if file.endswith(".wav"):
                src.append(os.path.join(root, file))

    for location in src:
        file_name = location.split("/")[-1]
        os.rename(location, dst + file_name)


#### Main Loop ####
if os.path.isfile(text_path):
    y = []

    with open(text_path, "r") as f:
        content = f.read()
        content = content.split(",")
        for i in content:
            y.append(i)
        y.pop()

        pics(y[0], y[1])
        videos(y[0], y[2])
        document(y[0], y[3])
        zip(y[0], y[4])
        music(y[0], y[5])
else:
    x = []

    path_Download = input("Please Enter Download path: ")
    path_pics = input("please Enter Picture path: ")
    path_videos = input("please Enter Videos path: ")
    path_document = input("please Enter Document path: ")
    path_zip = input("please Enter ZIP path: ")
    path_music = input("please Enter Music path: ")

    x.append(path_Download)
    x.append(path_pics)
    x.append(path_videos)
    x.append(path_document)
    x.append(path_zip)
    x.append(path_music)

    for word in x:
        with open(text_path, "a+") as f:
            f.write(word + ",")

    pics(path_Download, path_pics)
    videos(path_Download, path_videos)
    document(path_Download, path_document)
    zip(path_Download, path_zip)
    music(path_Download, path_music)
