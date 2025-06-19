from odoo import http
from odoo.http import request


class LiveReplayController(http.Controller):

    @http.route(['/replay/<model("live.replay"):replay>'], type='http', auth='public', website=True)
    def replay_detail(self, replay, **kwargs):
        return request.render('live_replay_website.replay_detail_template', {
            'replay': replay,
            'products': replay.product_ids,
        })

