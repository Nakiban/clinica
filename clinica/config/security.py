from pwdlib import PasswordHash

pass_context = PasswordHash.recommended()


def create_hash(password: str):
    return pass_context.hash(password=password)


def verify_hash(password: str, hash: str):
    return pass_context.verify(password=password, hash=hash)
