def search_email(my_email, emails):
    for email in emails:
        if email == my_email:
            return True

    return False


with open('emails.txt') as fo:
    list_emails = fo.read().splitlines()

print(list_emails)
print(search_email('johnbob@aol.com', list_emails))
