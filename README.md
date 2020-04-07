# Introduction
A tool to automatically type input provided via a file. Simulates keypresses for the input and
writes out the file based on a user specified delimeter.

Inspired by the [this TikTok](https://vm.tiktok.com/t3X3SN/).

## Running the Code
First install the dependencies for the programming using the command below.
```
$ poetry install
```
The first time you run this, it will take a little bit.

Next, you can start the program by running
```
$ poetry run main <source file location> 
```

Then, the source will be printed as soon as you press the ESCAPE key.

## Example Execution

```
$ poetry run main example_inputs/fitness.txt --delimeter="\n"
```

This example will print out all the contents of fitness.txt in which after each newline the enter
key is pressed. The delimeter can be set to anything however.

Here is example of sending someone the contents of bubble.txt over messages.

![alt text](use_example/example.PNG)
## Input
The source is required which is the path the the file to type out. The optional parameter
"delimeter" can be provided to specify how to seperate the file.
