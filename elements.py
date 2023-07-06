import random
import os

def adjective():
    with open("adjectives.txt", "r") as file:
        data = file.read()
        words = data.split()
        word_pos = random.randint(0, len(words) - 1)
        return words[word_pos]

def adverb():
    with open("adverbs.txt", "r") as file:
        data = file.read()
        words = data.split()
        word_pos = random.randint(0, len(words) - 1)
        return words[word_pos]

def animal():
    with open("animals.txt", "r") as file:
        data = file.read()
        words = data.split()
        word_pos = random.randint(0, len(words) - 1)
        return words[word_pos]

def namer():
    with open("names.txt", "r") as file:
        data = file.read()
        words = data.split()
        word_pos = random.randint(0, len(words) - 1)
        return words[word_pos]

def noun():
    with open("nouns.txt", "r") as file:
        data = file.read()
        words = data.split()
        word_pos = random.randint(0, len(words) - 1)
        return words[word_pos]

def nounb():
    with open("noun2.txt", "r") as file:
        data = file.read()
        words = data.split()
        word_pos = random.randint(0, len(words) - 1)
        return words[word_pos]

'''def madlib():
    directory = os.path.join(os.getcwd(), "madlibs")
    file_names = [file for file in os.listdir(directory) if file.endswith(".txt")]
    selected_file = random.choice(file_names)
    file_path = os.path.join(directory, selected_file)
    with open(file_path, 'r') as file:''''
