from flask import Flask
from dotenv import load_dotenv
from log.log import setup_logging

load_dotenv('.env')  # load environment variables
setup_logging(default_path='log/config.yml')
app = Flask(__name__)
