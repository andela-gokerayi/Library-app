from django.core.mail import send_mail

"""
This module contains common helper methods
to be used in the book app
"""
def send_borrow_request_mail(user, book_name):
    msg = """
            A request is been made by %s to borrow the book "%s"
          """ %(user.username, book_name)

    send_mail("Book Lending request", msg, 'andela.library@andela.co',
          ['gbolahan.okerayi@andela.co', 'eniola.arinde@andela.co'])

def send_decline_mail(lender, book):
    name = lender.split('.')[0] or lender
    msg = """
            Hi %s,

             Your request to borrow the book "%s" has been declined.
             Please contact the Librarian for more info.
          """ %(name, book)

    send_mail("Book Request Declined", msg, 'andela.library@andela.co',
              [lender])
