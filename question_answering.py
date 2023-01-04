#!pip install transformers
from transformers import pipeline

question_answerign_model = pipeline('question-answering')

context = "Today I went to the store to purchase a carton of milk."
question = "What did I buy? "
question_answerign_model(context=context, question=question)

context[38:54]

context = "Out of all the colors, I like blue the best."
question = "What is my favorite color?"
question_answerign_model(context=context, question=question)

context = "Albert Einstein (14 March 1879 - 18 April 1955) was a German-born theoretical physicist, widely acknowledged to be one of the greatest physicist of all time. Einstein is best known for developing the theory of relativity, but he also made important contributions to the development of the theory of quantum mechanics. Relativity and quantum mechanics are together the two pillars of modern physics."

question = "When was Albert Einstein born? "
question_answerign_model(context=context, question=question)

question = "What was Albert Einstein's occupation? "
question_answerign_model(context=context, question=question)

question = "What was Albert Einstein best known for? "
question_answerign_model(context=context, question=question)

question = "What else has Albert Einstein contributed to? "
question_answerign_model(context=context, question=question)

question = "What are the two pillars of modern physics? "
question_answerign_model(context=context, question=question)

question = "Where was Albert Einstein born? "
question_answerign_model(context=context, question=question)

question = "What is peanut butter made of? "
question_answerign_model(context=context, question=question)

