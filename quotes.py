from quote import quote
import random

random_author = random.randint(0,6)
random_quote = random.randint(0,6)

authors = ["Ray Bradbury", "Alice Walker", "Stephen Hawking", "Steve Jobs", "Coco Chanel", "Anita Roddick", "Helen Keller", ]
result = quote(authors[random_author], limit=7)

famous_quote = result[random_quote]["quote"] + "-" + result[random_quote]["author"]
