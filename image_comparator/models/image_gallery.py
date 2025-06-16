from odoo import models, fields, api

class ImageGallery(models.Model):
    _name = 'image.gallery'
    _description = 'Galerie d\'images'

    name = fields.Char(string="Nom", required=True)
    image = fields.Binary(string="Image", attachment=True)
    active = fields.Boolean(default=True)