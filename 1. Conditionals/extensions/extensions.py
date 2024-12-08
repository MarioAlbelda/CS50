def main():
    extension = input("File name: ").lower().strip()
    if gif(extension):
        print("image/gif")
    elif jpg_jpeg(extension):
        print("image/jpeg")
    elif png(extension):
        print("image/png")
    elif pdf(extension):
        print("application/pdf")
    elif txt(extension):
        print("text/plain")
    elif zp(extension):
        print("application/zip")
    else:
        print("application/octet-stream")

def gif(ext):
    return ext.endswith(".gif")

def jpg_jpeg(ext):
    return ext.endswith(".jpg") or ext.endswith(".jpeg")

def png(ext):
    return ext.endswith(".png")

def pdf(ext):
    return ext.endswith(".pdf")

def txt(ext):
    return ext.endswith(".txt")

def zp(ext):
    return ext.endswith(".zip")

main()
