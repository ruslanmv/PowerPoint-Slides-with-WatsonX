from Generator.pptcodegenerator import PptCodeGenerator
from Generator.structuregenerator import StructureGenerator


def main():
    structure_gen = StructureGenerator()
    ppt_gen = PptCodeGenerator()

    # This is the meeting summary
    text = "meeting_email"

    structure = structure_gen.generate_structure(text)
    code = ppt_gen.generate_code(structure)


if __name__ == "__main__":
    main()
