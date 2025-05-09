import os
from neo4j import GraphDatabase
from dotenv import load_dotenv
from llama_index.llms.ollama import Ollama

load_dotenv()


neo4j_driver = GraphDatabase.driver(os.environ.get("NEO4J_URI"),
    auth=(os.environ.get("NEO4J_USERNAME"), os.environ.get("NEO4J_PASSWORD")),
)

ai_client = Ollama(model="llama3", temperature=0)