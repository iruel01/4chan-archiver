#!/bin/env python2.7

import sys
import os
from subprocess import call

current_threads = {}
greet = "4chan image archiver - Alice (iruel01 on github)"
help_msg = "type help for usage"
usage = "add thread <board letter(s)> <thread number>\nlist threads <board letter(s)>\nremove thread <board letter(s)> <thread number>\nupdate thread <board letter(s)> <thread number>\n\exit"
url_str_main = "boards.4chan/"
url_str_res = "res/"

def main():
	print greet
	print help_msg
	input_str = ""

	while input_str != "exit":
		input_str = prompt()

		if input_str == "help":
			usage()

		choose_op(input_str)

def usage():
	print usage

def prompt():
	input_str = ""
	input_str = raw_input("> ")

	return input_str

def choose_op(input_str):
	args = input_str.split(' ')

	if args[0] == "add" and args[1] == "thread":
	elif args[0] == "list" and args[1] == "thread":
	elif args[0] == "remove" and args[1] == "thread":
	elif args[0] == "update" and args[1] == "thread":

def add(board_letter, board_number):

def list(board_letter):

def remove(board_letter, board_number):

def update(board_letter, board_number):
	new_string = url_str_main + board_letter + url_str_res + board_number
	call(["./dta.sh", new_string, board_letter, board_number])




		
