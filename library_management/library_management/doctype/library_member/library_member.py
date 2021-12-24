# Copyright (c) 2021, Mrinal and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class LibraryMember(Document):
	
	# This method will run everytime a doc is saved
	def before_save(self):
		
		if self.last_name == None:
			self.full_name = self.first_name
		else:
			self.full_name = '{} {}'.format(self.first_name, self.last_name) 
