#!/usr/bin/env python3

import pandas as pd
import random

def game_initialization():
  """This function need to run first before game is started.

  Return the index, category, answer, question, answer_in_char, and
  number_blank_char.

  index is row number of the question and answer in dataset.

  category is group of questions and answers game.

  answer is the answer key of the question that asked.

  question is the question that will be asked and displayed.

  answer_in_char is the answer in character list.

  number_blank_char is initial number of character.

  >>> _ = game_initialization()
  index : 92
  category : animal
  answer : rabbit
  question : ['_ _ _ _ _ _']
  answer_in_char : "[['r', 'a', 'b', 'b', 'i', 't']]"
  number_blank_char : 6

  >>> _ = game_initialization()
  index : 73
  category : animal
  answers : komodo dragon
  question : "['_ _ _ _ _ _', '_ _ _ _ _ _']"
  answer_in_char : "[['k', 'o', 'm', 'o', 'd', 'o'], ['d', 'r', 'a', 'g', 'o', 'n']]"
  number_blank_char : 12

  """

  df = pd.read_csv('hangman_dataset.csv')

  index = random.randint(1,len(df))
  category = df['category'][index]
  answer = df['answer'][index]
  question = df['question'][index]
  answer_in_char = df['answer_in_char'][index]
  number_blank_char = df['number_blank_char'][index]

  return index, category, answer, question, answer_in_char, number_blank_char


class Hangman:

  def __init__(self, category, answer, question, answer_in_char, number_blank_char):
    self.category = category
    self.answer = answer
    self.question = question
    self.answer_in_char = answer_in_char
    self.number_blank_char = number_blank_char

  def check_input(self, input_):
    if input_ in self.answer_in_char:
      print('true')
    else:
      print('false')

  def say(self):
    print('Your answer is {}'.format(self.answer))


_ = game_initialization()
game = Hangman(_[1], _[2], _[3], _[4], [5])

#game = Hangman('animal', 'orang utan', "['_ _ _ _ _', '_ _ _ _']", "[['o', 'r', 'a', 'n', 'g'], ['u', 't', 'a', 'n']]", 9)

#game.check_input('g')
print(game.__dict__)