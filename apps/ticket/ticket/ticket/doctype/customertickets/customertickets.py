# Copyright (c) 2024, agmah and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import  now

class CustomerTickets(Document):
	def set_user_and_timestamp(self):
		self._original_modified = self.modified
		self.modified = now()
		# self.modified_by = frappe.session.user
		self.modified_by = "Hello hunny"
		print("hello hunny printed")

		# We'd probably want the creation and owner to be set via API
		# or Data import at some point, that'd have to be handled here
		if self.is_new() and not (
			frappe.flags.in_install or frappe.flags.in_patch or frappe.flags.in_migrate
		):
			self.creation = self.modified
			self.owner = self.modified_by

		for d in self.get_all_children():
			d.modified = self.modified
			d.modified_by = self.modified_by
			if not d.owner:
				d.owner = self.owner
			if not d.creation:
				d.creation = self.creation

		frappe.flags.currently_saving.append((self.doctype, self.name))
