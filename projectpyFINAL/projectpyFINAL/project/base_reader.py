from project.dec import color_decorator

class CustomObject:
    def __init__(self, filename):
        self.filename = filename

    def __iter__(self):
        with open(self.filename, 'r') as f:
            for line in f:
                yield line.rstrip('\n')

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, value):
        if not value.endswith('.txt'):
            raise ValueError("Only .txt files are allowed.")
        self._filename = value

    @staticmethod
    def file_extension(filename):
        return filename.split('.')[-1]

    @classmethod
    def from_file(cls, filename):
        return cls(filename)

    @color_decorator("cyan")
    def __str__(self):
        return f"<CustomObject: {self._filename}>"