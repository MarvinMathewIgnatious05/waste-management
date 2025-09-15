def is_customer(user):
    return user.is_authenticated and user.role == 0