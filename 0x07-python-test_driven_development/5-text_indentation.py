#!/usr/bin/python3

"""
TextIndentation module
"""


def text_indentation(text):
   """
   prints a text with 2 new lines after
   each of those characters:
   '.' '?' ':'

   Args:
   text (str): a given string

   Raises:
   TypeError: if argument passes is
   not a string

   """
   if not isinstance(text, str):
       raise TypeError("text must be a string")

   string = ""
   for c in text:
       string += ":?":
           print(string.lstrip(), end="\n\n")
           string = ""
           print(string.lstrip(), end='')
