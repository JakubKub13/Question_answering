#!pip install transformers
from transformers import pipeline

question_answerign_model = pipeline('question-answering')