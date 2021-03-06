##
#    Copyright (C) 2013 Jessica Tallon & Matthew Molyneaux
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
##

from django.utils.translation import ugettext as _
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponseRedirect

def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/user/home")

    context = {
        "page":_("Home"),
        "registration_enabled":settings.ENABLE_REGISTRATION,
    }

    return render(request, "index.html", context)
