# Author: Jason Smith
# Date: May 21, 2023
# Title: MTG Catalog
# Purpose: This program creates and edits a catalog of MTG cards. This allows the user to easily see what cards are in
# their collection and print them for viewing outside of this program.

class TextFile:
	"""Represents an instance of a text file."""
	def __init__(self, name):
		self.name = name

	def read_file(self):
		"""Reads a text file."""
		pass

	def write_file(self):
		"""Writes to a text file."""
		pass

	def print_file(self):
		"""Prints a text file."""
		pass

	def open_file(self):
		"""Opens a file on the user's computer."""
		pass


class Card:
	"""Represents an instance of a card."""
	def __init__(self, name):  # more needed for card characteristics
		self.name = name

	def get_name(self):
		pass

	def set_name(self):
		pass


class Catalog(TextFile):  # possibly redundant class
	"""Represent an instance of a catalog."""
	def __init__(self, name):
		super().__init__(name)
		pass
