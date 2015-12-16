#!/usr/bin/env python
import copy,string,sys
def main():
	print;print '#### lc.py: your letter-cheater companion ####'
	with open('wordlist.txt','r') as f:		#get word list: 172,822 words
		doc = f.read().split()
	master_list = [[] for x in range(29)]	#create master_list
	for word in doc:
		master_list[len(word)].append(word)		#sort master_list by word length
	print 'This list contains:',len(doc),'words'
	#for wordlist in range(len(master_list)):
	#	print 'Words with',wordlist,'letters:',len(master_list[wordlist])
	current_list = copy.copy(master_list)		#copy master_list (unchanging) into current_list for sequential truncation
	valid_letters = list(string.ascii_lowercase + string.ascii_uppercase)
	input_letters = ''
	while 1:
		def get_letters():			
			new_letters = raw_input('Enter new letters or type ! to quit: ')	#get new letters from user
			new_letters = new_letters.lower()
			if new_letters == '!':
				sys.exit()
			for each_letter in new_letters:
				if each_letter not in valid_letters:	#validate letters
					return False
			else:
				return new_letters
		new_letters = False
		while not new_letters:
			new_letters = get_letters()
		input_letters += new_letters
		anagrams = []
		print 'input_letters:',input_letters
		has_entries = False
		for each_list in current_list:		#check length-based word list for matches
			mask = ''		
			for each_word in each_list:			#check each word in each list
				current_word = list(each_word)
				for each_letter in input_letters:		#ensure all input letters are present in word
					if each_letter in current_word:
						current_word.pop(current_word.index(each_letter))	#if letter is found, pop letter to avoid duplicates
					else:
						mask+='0'	#not all letters found; generate 0 pointer to ensure this word is not added to trunc_list
						break
				else:
					if len(current_word) == 0:
						anagrams.append(each_word)
					mask+='1'	#all input_letters are present in this word; generate mask pointer to add to trunc_list
					has_entries = True
			trunc_list = []
			for pointer in range(len(mask)):
				if mask[pointer] == '1':
					trunc_list.append(each_list[pointer])	#generate new trunc_list based on mask
			current_list[current_list.index(each_list)] = trunc_list	#replace specific length-based list in current_list with new trunc_list
		if has_entries == False:
			print 'No words found with specified letters'
			sys.exit()
		else:
			word_count = 0
			print 'Valid words available:'		#print updated word list
			for each_list in current_list:
				if each_list:
					word_count += len(each_list)
					print '',len(each_list),len(each_list[0]),'letter words:'
					print '',' '.join(each_list)
			print;print 'Total number of words that contain \'',input_letters,'\' in any order:',word_count
			print 'Anagrams of ',input_letters,':',anagrams
			print		
					

if __name__ == '__main__':
	main()