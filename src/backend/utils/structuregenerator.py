from utils.generator import Generator
from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes
import requests
import logging


class StructureGenerator(Generator):

    structure_prompt = f"""You are really good at writing and analyzing a meeting from its summary email.
            Write the structure of a powerpoint presentation given the summary email.
            Do not write any note. 
            You have also to title and content of the slides. 
            You cannot create false information. You cannot create false dates.
            Write the powerpoint in a structured way."""

    def __init__(self):
        super().__init__(ModelTypes.LLAMA_2_70B_CHAT)

    def generate_structure(self, text):
        logging.info("Sending prompt for structure")

        inst_prompt = f"""[INST] <<SYS>>  
        {StructureGenerator.structure_prompt}
        <</SYS>>
        Create the powerpoint from the following transcripts: {text}
        [/INST]
        """
        result = self.llm_model.generate(
            inst_prompt)['results'][0]['generated_text']
        logging.info("Obtained result")
        return result
