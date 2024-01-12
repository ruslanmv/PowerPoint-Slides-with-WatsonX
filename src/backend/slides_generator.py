from utils.pptcodegenerator import PptCodeGenerator
from utils.pptcodegenerator import extract_slides
from utils.structuregenerator import StructureGenerator
from utils.pptxgen import pptxgenerator
import logging
from io import StringIO
import sys


class PowerPoint():

    def __init__(self, filepath: str = "./tmp/presentation.py"):
        self.code = ""
        self.structure = ""
        self.filepath = filepath

    def __save_code_to_file(self):
        with open(self.filepath, "w") as file:
            file.write(self.code)

    def __compile_code(self):
        # Save the original stdout
        original_stdout = sys.stdout
        # Redirect stdout to a StringIO object
        sys.stdout = buffer = StringIO()
        try:
            # Execute the generated code
            exec(self.code)
        except Exception as e:
            print(f"Error executing generated code: {e}")
        finally:
            # Restore the original stdout
            sys.stdout = original_stdout

        return buffer.getvalue()

    def slides(self, text: str):
        structure_gen = StructureGenerator()
        ppt_gen = pptxgenerator()
        self.structure = structure_gen.generate_structure(text)

        ppt_gen.generate_code(self.structure)

        print(self.structure)

        self.__save_code_to_file()

        self.__compile_code()


if __name__ == "__main__":

    name_of_file = sys.argv[0]

    ppt = PowerPoint()

    with open(name_of_file, 'r') as txt:
        text = txt.readlines()
        text = "\n".join(text)
        ppt.slides(text)
