class baseElement():
    """Base Element : Has all the Methods and atributes for creating
    new features"""
    def __init__(self, marker=""):
        self.marker = marker
        self.html = "<p>{}</p>\n"

    def fill(self, string):
        self.export = self.html.format(string)

    def returnExport(self):
        return self.export

if __name__ == "__main__":
    obj = baseElement()
    obj.fill("Aditya is cool")
    print(obj.export)
