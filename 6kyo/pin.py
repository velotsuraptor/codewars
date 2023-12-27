def validate_pin(pin):
    if '+' or '-' or ' ' in pin:
        return False
    try:
        int(pin)
    except:
        return False
    if len(pin) == 4 or len(pin) == 6:
        return True


print(validate_pin('1124'))
