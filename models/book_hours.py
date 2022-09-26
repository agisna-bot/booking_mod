from unicodedata import name
from odoo import fields, api, models

class BookHours(models.Model):
    _name = 'book.hours'
    _description = 'Book Hours'

    name = fields.Float(string='Jam Pemesanan', required=True)