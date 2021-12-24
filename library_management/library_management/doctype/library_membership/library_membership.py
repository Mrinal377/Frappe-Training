# Copyright (c) 2021, Mrinal and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

# let's write code that will make sure whenever a Library Membership is created, there is no active membership for the Member.

class LibraryMembership(Document):

	# Checks before submitting Document
	def before_submit(self):
		exist = frappe.db.exists('Library Membership', {'library_member': self.library_member, 'docstatus': 1, 'to_date' : ('>', self.from_date)})

		if exist:
			frappe.throw('There is an active membership for this member') 

		# Let's make the change in Library Membership such that, the To Date automatically computed based on the Loan Period and the From Date.
		loan_period = frappe.db.get_single_value('Library Settings', 'loan_period')
		self.to_date = frappe.utils.add_days(self.from_date, loan_period or 30)
