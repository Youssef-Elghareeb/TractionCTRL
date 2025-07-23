import os
from project.base_reader import CustomObject

class ExtendedCustomObject(CustomObject):
    def __init__(self, filename):
        super().__init__(filename)

    def concatenate(self, *readers, output_filename="merged_multi.txt"):
        """Concatenate content of CustomObject instances into one file."""
        with open(output_filename, 'w') as outfile:
            with open(self.filename, 'r') as f:
                outfile.write(f.read())
                outfile.write("\n")
            for reader in readers:
                if not isinstance(reader, CustomObject):
                    raise TypeError("All arguments must be CustomObject instances.")
                with open(reader.filename, 'r') as f:
                    outfile.write(f.read())
                    outfile.write("\n")
        return ExtendedCustomObject(output_filename)

    def __add__(self, other):
        """Override + to use a safe filename for merged output."""
        base1 = os.path.splitext(os.path.basename(self.filename))[0]
        base2 = os.path.splitext(os.path.basename(other.filename))[0]
        merged_name = f"{base1}_plus_{base2}.txt"
        merged_path = os.path.join(os.path.dirname(self.filename), merged_name)
        return self.concatenate(other, output_filename=merged_path)