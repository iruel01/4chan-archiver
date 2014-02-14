#!/bin/env python2.7

import sys
import os
from subprocess import call
import urllib2

current_threads = {}
greet = "4chan image archiver - Alice (iruel01 on github)"
help_msg = "type help for usage"
usage = "add thread <board letter(s)> <thread number>\nlist threads <board letter(s)>\nremove thread <board letter(s)> <thread number>\nupdate thread <board letter(s)> <thread number>\n\exit"
url_str_main = "boards.4chan/"
url_str_res = "res/"

#read in the list from a file
def update_dictionary():
	pass

#write the current threads
def update_list():
	pass

def usage():
	print usage

def prompt():
	input_str = ""
	input_str = raw_input("> ")

	return input_str

def choose_op(input_str):
	args = input_str.split(' ')

	if args[0] == "add" and args[1] == "thread":
		add(args[2], args[3])
	elif args[0] == "list" and args[1] == "thread":
		list(args[2])
	elif args[0] == "remove" and args[1] == "thread":
		remove(args[2], args[3])
	elif args[0] == "update" and args[1] == "thread":
		update(args[2], args[3])
	elif args[0] == "help":
		usage()
	else:
		usage()

def add(board_letter, board_number):
	new_string = url_str_main + board_letter + url_str_res + board_number

def list(board_letter):
	print "current threads"
	if board_letter in current_threads:
		print current_threads[board_letter]
	else:
		"no threads for that board"

def remove(board_letter, board_number):
	if check_url(board_letter, board_number):
		current_threads[board_letter].remove(board_number)
	else:
		print "thread does not exist"
		return

def check_if(board_letter, board_number):
	if board_number in current_threads[board_letter]:
		return true
	else:
		return false

def update(board_letter, board_number):
	if not check_if:
		print "thread does not exist"
		return

	new_string = url_str_main + board_letter + url_str_res + board_number
	if check_url():
		call(["./dta.sh", new_string, board_letter, board_number])
	else:
		print "thread is 404\n removing thread"
		remove(board_letter, board_number)

def check_url(new_string):
	req = urllib2.Request(new_string)
	try:
		resp = urllib2.urlopen(req)
	except urllib2.URLError, e:
		if e.code == 404:
			return false
		else:
			return true
	else:
		return false

def main():
	print greet
	print help_msg
	input_str = ""

	update_dictionary()

	while input_str != "exit":
		input_str = prompt()

		if input_str == "help":
			usage()

		choose_op(input_str)

	update_list()

main()