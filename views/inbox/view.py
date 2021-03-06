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

from django.utils.translation import ugettext as _
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import Http404

from inboxen.helper.mail import get_email, clean_html
from inboxen.models import Inbox, Email, Domain

@login_required
def view(request, email_address, emailid):

    inbox, domain = email_address.split("@", 1)
    
    try:
        inbox = Inbox.objects.get(inbox=inbox, domain__domain=domain, user=request.user)
    except Inbox.DoesNotExist:
        raise Http404

    try:
        email = get_email(request.user, emailid, read=True)
    except Email.DoesNotExist:
        raise Http404

    from_address = email["from"].split("@", 1)

    if email["plain"]:
        plain_message = email["body"]
    else:
        plain_message = ""
        # also because a html email lets parse
        if "body" in email:
            email["body"] = clean_html(email["body"])
        else:
            email["body"] = "" # emails can have no body

    context = {
        "page":email["subject"],
        "email":email,
        "plain_message":plain_message,
        "user":request.user,
    }
 
    return render(request, "inbox/email.html", context)
