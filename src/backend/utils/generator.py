import os
from dotenv import load_dotenv
from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
import requests
import logging


class Generator():

    load_dotenv()

    def __init__(self, model):

        parameters = {
            GenParams.DECODING_METHOD: "greedy",
            GenParams.MAX_NEW_TOKENS: 1000,
            GenParams.STOP_SEQUENCES: ["\n\n\n"]
        }
        project_id = os.getenv("PROJECT_ID", None)
        credentials = {
            "url":  "https://eu-de.ml.cloud.ibm.com",
            "apikey": os.getenv("API_KEY", None)
        }
        credentials["token"] = Generator.__getBearer(
            credentials["apikey"])
        # Initialize the Watsonx foundation model
        self.llm_model = Model(
            model_id=model,
            params=parameters,
            credentials=credentials,
            project_id=project_id)

    @staticmethod
    def __getBearer(apikey):
        form = {'apikey': apikey,
                'grant_type': "urn:ibm:params:oauth:grant-type:apikey"}
        logging.info("About to create bearer")
        response = requests.post(
            "https://iam.cloud.ibm.com/oidc/token", data=form)
        if response.status_code != 200:
            logging.error("Bad response code retrieving token")
            raise Exception("Failed to get token, invalid status")
        json = response.json()
        if not json:
            logging.error("Invalid/no JSON retrieving token")
            raise Exception("Failed to get token, invalid response")
        logging.info("Bearer retrieved")
        return json.get("access_token")
