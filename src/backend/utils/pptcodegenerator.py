from utils.generator import Generator
from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes
import requests
import logging


class PptCodeGenerator(Generator):
    code_prompt = f"""You are really good at writing python code and using the library python-pptx.
            Write the code in python to create the powerpoint presentation given its structure.
            Answer only with python code ready to run.
            """

    def __init__(self):
        #super().__init__(ModelTypes.STARCODER)
        super().__init__(ModelTypes.LLAMA_2_70B_CHAT)

    def generate_code(self, text,options):
        logging.info("Sending prompt for code")
        inst_prompt = f"""<s>[INST] <<SYS>>  
        {PptCodeGenerator.code_prompt}
        <</SYS>>
        {options}
        Create the python code given this structure: {text}
        Code:
        [/INST]
        """
        result = self.llm_model.generate(
            inst_prompt)['results'][0]['generated_text']
        logging.info("Obtained result")
        return result

def extract_slides(text):
    slides = []
    lines = text.split("\n")
    current_slide = ""

    for line in lines:
        if line.startswith("Slide"):
            if current_slide:
                slides.append(current_slide)
                current_slide = ""
            current_slide = line
        elif current_slide:
            current_slide += "\n" + line

    if current_slide:
        slides.append(current_slide)
    
    return slides