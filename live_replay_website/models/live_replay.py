from odoo import models, fields,api
from odoo.addons.http_routing.models.ir_http import slug as odoo_slug
import logging


class LiveReplay(models.Model):
    _name = 'live.replay'
    _description = 'Rediffusion de Live'
    _inherit = ['website.published.mixin']
    _order = 'date desc'

    name = fields.Char(required=True)
    date = fields.Date(required=True)
    video_url = fields.Char('Lien vidéo')
    image = fields.Image('Image de couverture')
    product_ids = fields.Many2many('product.product', string='Produits présentés')
    slug = fields.Char(compute='_compute_slug', store=True,readonly=True, index=True, unique=True)


    @api.depends('name')
    def _compute_slug(self):
        for record in self:
            try:
                if record.id and record.name:
                    record.slug = odoo_slug((record.id, record.name))
                else:
                    record.slug = False
            except Exception as e:
                        _logger = logging.getLogger(__name__)
                        _logger.error("Erreur lors du calcul du slug : %s", str(e))
                        record.slug = False