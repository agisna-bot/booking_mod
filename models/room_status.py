from odoo import api, fields, models
 
class RoomStatus(models.Model):
    _name = 'room.status'
    _description = 'Room Status'
     
    name = fields.Char(string='Status Ruangan', required=True)