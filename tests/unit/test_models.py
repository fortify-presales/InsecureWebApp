"""
        InsecureWebApp - an insecure Python/Flask Web application

        Copyright (C) 2024-2025  Kevin A. Lee (kadraman)

        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation, either version 3 of the License, or
        (at your option) any later version.

        This program is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU General Public License for more details.

        You should have received a copy of the GNU General Public License
        along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import pytest

def test_new_user(new_user):
    """
    Test the User model of InsecureWebApp
    """
    assert new_user.email == 'user5@localhost.com'
    assert new_user.first_name == 'Steve'
    assert new_user.last_name == 'Shopper'


def test_new_product(new_product):
    """
    Test the Product model of InsecureWebApp
    """
    assert new_product.code == 'SWA543-A343-00462'
    assert new_product.name == 'Pilex One'
