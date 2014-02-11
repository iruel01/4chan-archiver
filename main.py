#!/bin/env python2.7

import sys
import os

current_threads = {}
greet = "4chan image archiver - Alice (iruel01 on github)"
help_msg = "type help for usage"
usage = "add thread <thread url>\nlist threads <board letter(s)>\nremove thread <board letter(s)> <thread number>\nupdate thread <board letter(s)> <thread number>\n\exit"


def main():
	print greet
	print help_msg
	input_str = ""

	while input_str != "exit":
		input_str = prompt()



def usage():
	print usage

def prompt():
	input_str = ""
	input_str = raw_input("> ")

	return input_str

def choose_op(input_str):
	args = input_str.split(' ')

	if args[0] == "add" and args[1] == thread:
		
