def validate_wifi_password(key):
    if not isinstance( key , str) or (len(key)<12) :
        return False
    else:
        return True


        