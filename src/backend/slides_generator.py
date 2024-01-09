from utils.pptcodegenerator import PptCodeGenerator
from utils.pptcodegenerator import extract_slides
from utils.structuregenerator import StructureGenerator
from utils.pptxgen import pptxgenerator
import os
from io import StringIO
import sys


def save_code_to_file(code, filename="./tmp/presentation.py"):
    with open(filename, "w") as file:
        file.write(code)


def compile_code(code):
    # Save the original stdout
    original_stdout = sys.stdout
    # Redirect stdout to a StringIO object
    sys.stdout = buffer = StringIO()
    try:
        # Execute the generated code
        exec(code)
    except Exception as e:
        print(f"Error executing generated code: {e}")
    finally:
        # Restore the original stdout
        sys.stdout = original_stdout

    return buffer.getvalue()


def main(input):
    structure_gen = StructureGenerator()
    # ppt_gen = PptCodeGenerator()
    ppt_gen = pptxgenerator()
    text = input
    structure = structure_gen.generate_structure(text)
    # print("Generated Struture:", structure)

    code = ppt_gen.generate_code(structure)

    save_code_to_file(code, "./tmp/presentation.py")

    output = compile_code(code)
    #print("Output:\n", output)

    if os.path.exists(f"presentation.pptx"):
        print(f"presentation was created successfully.")
    else:
        print(f"Failed to create presentation.pptx")

    """
    slides = extract_slides(structure)
    # print("Generated slides:", slides)
    print("Generated strucure done")
    number_slides = len(slides)
    for n in range(number_slides):
        print("Creating the code for slide number: ", n)
        slide = slides[n]
        code = ppt_gen.generate_code(slide, n)
        print("Code Generated:", code)
        # print(code)
        # Save the generated code to slide.py
        save_code_to_file(code, "./tmp/slide_{}.py".format(n))
        print("The generated code has been saved to slide_{}.py".format(n))
        # Compile and run the generated code
        output = compile_code(code)
        print("Output:\n", output)

        # Check if the slide.pptx file was created
        if os.path.exists(f"slide_{n}.pptx"):
            print(f"slide_{n} was created successfully.")
        else:
            print(f"Failed to create slide_{n}.pptx")
    """


test = '''
Subject: Summary of Meeting - Financial Results and Strategies

Dear Team,
I hope this email finds you well. I would like to provide a summary of our recent meeting regarding our financial results for the third quarter and our strategies for the upcoming year.
Giacomo opened the meeting by welcoming everyone and introducing the agenda. Andrea then presented the financial results, highlighting a net profit of 10 million euros, a 5% increase compared to the same period last year. He also mentioned improvements in our net interest margin, efficiency ratio, and return on equity.
Paola commended the team on these excellent results and asked about the key factors contributing to them. Andrea explained that our ability to attract new customers, particularly in the small and medium-sized businesses segment, careful cost and risk management, and investment in digital innovation were the main drivers.
After discussing the financial results, Giacomo shifted the focus to our strategies for the next year. Marco outlined our priorities, which include consolidating our market position, increasing profitability, and enhancing our reputation. To achieve these goals, we need to continue focusing on customer needs, developing new products and services, strengthening our online presence, and supporting the ecological and social transition. He also acknowledged the challenges of increasing competition, adapting to new regulations, and managing economic uncertainty related to the pandemic.
Giacomo expressed his satisfaction with the clear and coherent strategies presented. He invited the team to add any additional comments or questions. Director E took the opportunity to ask about the financing of our digital innovation projects – whether we plan to increase our capital or rely on external loans. Andrea responded that, currently, our financial position is strong, and we have good access to capital markets. Therefore, there are no plans to increase capital or seek external loans. However, we will continuously monitor our financial situation and evaluate opportunities as they arise.
Giacomo concluded the meeting by thanking everyone for their participation and wishing them a good day. Andrea echoed his sentiments and extended his thanks as well.
If you have any further questions or need additional information, please don't hesitate to reach out.
Best regards,
'''

if __name__ == "__main__":
    text = test
    main(text)
