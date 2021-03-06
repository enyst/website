##
#    Copyright (C) 2013 Jessica Tallon & Matt Molyneaux
#   
#    This file is part of Inboxen.
#
#    Inboxen is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Inboxen is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with Inboxen.  If not, see <http://www.gnu.org/licenses/>.
##

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404

from inboxen.models import Email

def delete(request, email_address, emailid):

    emailid = int(emailid, 16)    
    inbox, domain = email_address.split("@", 1)

    try:
        email = Email.objects.filter(id=emailid, user=request.user).only("id").get()
    except Email.DoesNotExist:
        raise Http404

    email.delete()

    return HttpResponseRedirect("/inbox/%s/" % email_address)

