


def is_good_password(s):
    if len(s) >= 9 and any(i.isdigit() for i in s) and s.upper() != s and s.lower() != s:
        return True
    return False

print(is_good_password('41157082'))
print(is_good_password('мойпарольсамыйлучший'))
print(is_good_password('МойПарольСамыйЛучший111'))

