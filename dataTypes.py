class baseElement():
    """Base Element : Has all the Methods and atributes for creating
    new features"""
    def __init__(self):
        self.marker = ""
        self.html = "<p>{}</p>\n"

        # Is element sensitive to newline i.e. Newline is needed before it?
        self.isNewline = True
        # Can the element be used intext?
        self.isIntext = False

    def fill(self, string):
        self.export = self.html.format(string)

    def returnExport(self):
        return self.export


class bold(baseElement):
    """Bold Element"""
    def __init__(self):
        self.marker = "**"
        self.html = "<b>{}</b>"
        self.isNewline = False
        self.isIntext = True


class italic(baseElement):
    """Italic Element"""
    def __init__(self):
        self.marker = "*"
        self.html = "<i>{}</i>"
        self.isNewline = False
        self.isIntext = True

if __name__ == "__main__":
    obj = bold()
    obj2 = italic()
    obj.fill("Aditya is cool")
    s = obj.export
    obj2.fill("None is cooler")
    s += obj2.export
    print(s)
