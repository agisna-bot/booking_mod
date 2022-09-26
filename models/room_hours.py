from odoo import api, fields, models
 
class RoomHours(models.Model):
    _name = 'room.hours'
    _description = 'Room Hours'
     
    name = fields.Float(string='Durasi Pemesanan', required=True)