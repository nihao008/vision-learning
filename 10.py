paths = ["a.jpg", "b.png", "c.jpg", "d.txt", "e.JPG"]

def filter_jpg(paths):
    return [i for i in paths if i.endswith(".jpg")]

print(filter_jpg(paths))
