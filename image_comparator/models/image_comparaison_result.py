from odoo import models, fields

class ImageComparisonResult(models.Model):
    _name = 'image.comparison.result'
    _description = 'Comparison Result'

    comparator_id = fields.Many2one('image.comparator', string='Comparator', required=True)
    gallery_image_id = fields.Many2one('image.gallery', string='Gallery Image', required=True)
    similarity_score = fields.Float(string='Score de similarité', readonly=True)