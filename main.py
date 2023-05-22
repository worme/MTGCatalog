# Author: Jason Smith
# Date: May 21, 2023
# Title: MTG Catalog
# Purpose: This program creates and edits a catalog of MTG cards. This allows the user to easily see what cards are in
# their collection and print them for viewing outside of this program.

class TextFile:
	"""Represents an instance of a text file."""
	def __init__(self, file_path):
		self.file_path = file_path

	def read_file(self, file_name):
		"""Reads a text file."""
		try:
			with open(file_name, 'r') as file:
				print(f"Reading the file called {file_name} ...")
				for line in file:
					print(line.strip())
		except FileNotFoundError:
			print("The file was not found.")
			print(f"Creating a new file called {file_name} ...")
			self.write_file(file_name)

	def write_file(self, file):  # card
		"""Writes to a text file."""
		with open(file, 'w') as outfile:
			outfile.write("test")  #  self.previous_content + '\n' + card

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

	# --------------- tests --------------------

	# read
	file = input("Enter the file name: ")
	file_obj = TextFile(file)
	file_obj.read_file(file)

	# write
	# file_obj.write_file("This is a test doc!")


if __name__ == '__main__':
	main()
