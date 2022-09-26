from odoo import api, fields, models
 
class RoomList(models.Model):
    _name = 'room.list'
    _description = 'Room List'
     
    name = fields.Char(string='Nama Ruangan', required=True)
    kode = fields.Char(string='Kode', required=True)
    # status one2many
