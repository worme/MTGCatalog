# Author: Jason Smith
# Date: May 21, 2023
# Title: MTG Catalog
# Purpose: This program creates and edits a catalog of MTG cards. This allows the user to easily see what cards are in
# their collection and print them for viewing outside of this program.

class TextFile:
	"""Represents an instance of a text file."""
	def __init__(self, file_path, previous_content):
		self.file_path = file_path
		self.previous_content = previous_content

	def read_file(self, file_path):
		"""Reads a text file."""
		try:
			with open(file_path, 'r') as file:
				self.previous_content = file.read()
		except FileNotFoundError:
			print("The file was not found.")

	def write_file(self, file, card):
		"""Writes to a text file."""
		with open(file, 'w') as outfile:
			outfile.write(self.previous_content + '\n' + card)

	def set_file(self, file_path):
		"""Opens a file on the user's computer."""
		self.file_path = file_path


class Card:
	"""Represents an instance of a card."""
	def __init__(self, name):  # more needed for card characteristics
		self.name = name

	def get_name(self):
		return self.name

	def set_name(self, name):
		self.name = name


def main():
	"""Main loop."""


if __name__ == '__main__':
	main()
