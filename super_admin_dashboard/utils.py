
def is_super_admin(user):
    return user.is_authenticated and (user.is_superuser or getattr(user, "role", None) == 2)