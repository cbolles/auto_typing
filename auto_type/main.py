"""
A tool that simulates keypresses based on a given input file. The program works by accepting a
source file containing the text and an optional delimeter for how to split up the text. The
program then creates an array of string based on the delimeter. Once the user presses the
ESCAPE key, each value in the array will be typed out seperated by newlines.

:author Collin Bolles:
"""
import keyboard
import argparse
from typing import List


def get_segments(delimeter: str, source_location: str) -> List[str]:
    """
    Takes in the location of the source file and returns a list of inputs that are split up based
    on the passed in delimeter
    :param delimeter: The delimeter to break up the input
    :param source_location: Path to file where source material exists
    """
    segments = []
    with open(source_location) as source_file:
        for line in source_file:
            for word in line.split(delimeter):
                segments.append(word.strip())
    return segments


def run_typing(segments: List[str]):
    """
    Function that handles typing the segments out.
    :param segments: The segments to write out seperated by newlines
    """
    for segment in segments:
        keyboard.write(segment)
        keyboard.press_and_release('enter')


def main():
    parser = argparse.ArgumentParser(description='''A tool to automatically type out a given piece
                                     of text''')
    parser.add_argument('source', action='store', help='''path to the source text that will be
                        typed out by the program''')
    parser.add_argument('--delimeter', action='store', help='''delimeter that will be used to split
                        up the text, by default will be split by newline''', default='\n')
    args = parser.parse_args()

    # Get the segments seperated based on the defined delimeter
    segments = get_segments(args.delimeter, args.source)

    # Setup listener to kick off running the typing function
    keyboard.add_hotkey('esc', lambda: run_typing(segments))

    # Wait until the escape key is pressed again
    keyboard.wait('esc')


if __name__ == '__main__':
    main()
