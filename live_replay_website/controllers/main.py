# from odoo import http
# from odoo.http import request


# class LiveReplayController(http.Controller):

#     @http.route(['/replay/<model("live.replay"):replay>'], type='http', auth='public', website=True)
#     def replay_detail(self, replay, **kwargs):
#         return request.render('hk_front.replay_detail_template', {
#             'replay': replay,
#             'products': replay.product_ids,
#         })
from odoo import http
from odoo.http import request

class ReplayController(http.Controller):

    @http.route('/replay/test', type='http', auth='public', website=True)
    def test_replay(self):
        return request.render('hk_front.replay_detail_template', {})
