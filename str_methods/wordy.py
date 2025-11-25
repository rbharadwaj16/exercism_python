question = "What is 50 divided by 2?"

question = question.removeprefix("What is")
question = question.removesuffix("?")
question = question.replace("by", "")
question = question.strip()
question = question.split()

print(question)
