from utils.generator import Generator
from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes
import requests
import logging


class PptCodeGenerator(Generator):

    code_prompt = f"""You are really good at writing python code and using the library python-pptx.
            Write the code in python to create the powerpoint presentation given its structure.
            Do not write any note. 
            You cannot create false information. You cannot create false dates.
            Write the python code in a structured way."""

    def __init__(self):
        super().__init__(ModelTypes.STARCODER)

    def generate_code(self, text):
        logging.info("Sending prompt for code")

        inst_prompt = f"""<s>[INST] <<SYS>>  
        {PptCodeGenerator.code_prompt}
        <</SYS>>
        Create the python code given this structure: {text}
        [/INST]
        """
        result = self.llm_model.generate(
            inst_prompt)['results'][0]['generated_text']
        logging.info("Obtained result")
        return result
