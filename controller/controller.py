# -*- encoding: utf-8 -*-

from odoo import http


class Configurator(http.Controller):

    # @http.route('/shop/product/chaise-urane-4', auth='public', website=True)
    # def index(self, **kw):
    #     Products = http.request.env['product.product']
    #     return http.request.render('website_sale_custom.index', {
    #         'products': Products.search([])})

    @http.route('/test/<model("product.product"):name>', auth='public', website=True)
    def name(self, name):
        Products = http.request.env['product.product']
        return http.request.render('website_sale_custom.index', {
            'products': Products.search([]),
            'name': name,
        })
