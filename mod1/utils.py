def user_name_extracter(email):
    return email[:email.find('@')]

if __name__ == '__main__':
    test_email = "vishwas@cloudthat.com"
    print(user_name_extracter(test_email))