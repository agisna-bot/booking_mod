from dataclasses import field
from odoo import api, fields, models
from datetime import datetime, timedelta
 
class RoomBook(models.Model):
    _name = 'room.book'
    _description = 'Room Booking'
     
    name = fields.Char(string='Kode Booking', required=True)
    
    # book_start = fields.Datetime(string='Waktu Mulai')
    # book_end = fields.Datetime(string='Waktu Selesai' , compute='_compute_time')

    # @api.depends('book_start', 'duration_id')
    # def _compute_time(self):
    #     for record in self:
    #         if record.book_start:
    #             record.book_end = record.book_start + timedelta(hours=int(record.duration_id))
    #         else:
    #             record.book_end = datetime.now() + timedelta(hours=int(record.duration_id)) 

    book_line_ids = fields.One2many('room.book.line', 'book_id', string='Book')

class RoomBookLine(models.Model):
    _name = 'room.book.line'
    _description = 'Room Booking Line'

    book_id = fields.Many2one('room.book', 'Book')
    room_id = fields.Many2one(comodel_name='room.list', string='Ruangan')
    book_date = fields.Date(string='Tanggal')
    duration_id = fields.Many2one(comodel_name='room.hours', string='Durasi Pemesanan')
    hours_id = fields.Many2one(comodel_name='book.hours', string='Jam Pemesanan')

    # @api.onchange('room_id')
    # def _room_id_change(self):