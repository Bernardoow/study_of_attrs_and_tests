# -*- coding: utf-8 -*-

import attr


@attr.s
class Coordinates(object):
    x = attr.ib(converter=int, type=int)

    @x.validator
    def check(self, attribute, value):
        if value < 0:
            raise ValueError(f"{attribute.name} must be positive")

    y = attr.ib(converter=int, type=int)

    @y.validator
    def check(self, attribute, value):
        if value < 10:
            raise ValueError(f"{attribute.name} must be positive")
