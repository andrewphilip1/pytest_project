import sys
import random
import string
import pytest
import argparse
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def generate_random_string():
    letters = string.ascii_lowercase
    random_string = ''
    for j in range(10):
        random_string = random_string+random.choice(letters)
    return random_string

# parser = argparse.ArgumentParser(description='number of strings to be generated')
# parser.add_argument('invalue', type=int, help='Input value for the number of strings to be generated')
# args = parser.parse_args()

def test_string_generator(invalue):
    list_of_random_strings = []
    for i in range (int(invalue)):
        list_of_random_strings.append(generate_random_string())

    list_of_random_strings.sort()
    logger.info(list_of_random_strings) #similar to printing 
    assert len(list_of_random_strings) == 10
    
