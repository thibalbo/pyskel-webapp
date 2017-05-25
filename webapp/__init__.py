from flask import Flask
from dotenv import load_dotenv

load_dotenv('.env')  # load environment variables
app = Flask(__name__)
