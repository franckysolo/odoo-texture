odoo.debug = true;

odoo.define('website_sale_custom', function (require) {
  'use strict';
  var Widget = require('web.Widget');
  var core = require('web.core');
  require('website.website');

  var TexturePicker = Widget.extend({
    template: 'website_sale_custom.index',
    init: function () {
      this.eventType = 'click touchstart';
    },
    start: function () {
      this.menu_dropdown();
      this.action_select();
    },
    menu_dropdown: function () {
      $('.texture-dropdown').on(this.eventType, function (e) {
        e.stopImmediatePropagation();
        if (!$(this).next().hasClass('is-open')) {
          $(this).addClass('is-active');
          $(this).next().addClass('is-open');
        } else {
          $(this).removeClass('is-active');
          $(this).next().removeClass('is-open');
        }
      });
    },
    action_select: function () {
      $('.texture-row').on(this.eventType, function (e) {
        // e.stopImmediatePropagation();
        var link = $(this);
        var icon = link.find('.status:first');
        var value = link.attr('data-value')
        var css = link.attr('data-class')
        $('#texture-text').html(value)
        $('#texture-preview').removeAttr('class').addClass(css)
        $('.texture-row').removeClass('is-selected');
        $('.status').addClass('hide');
        link.addClass('is-selected');
        icon.removeClass('hide')
      });
    }
  });

  var t = new TexturePicker();
  t.start();
  return t;
});
