# -*- coding: utf-8 -*-
from openerp.models import Model
from openerp.fields import Char


class holiday(Model):
    _name = "holidays.holiday"

    name = Char()