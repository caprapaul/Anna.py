#<------ Helper Methods ------>
def getScaledTime(extension, value):
    if extension.lower() == 's' or extension.lower() == 'seconds':
        return value
    elif extension.lower() == 'm' or extension.lower() == 'minutes':
        return value * 60
    elif extension.lower() == 'h' or extension.lower() == 'hours':
        return value * 3600
    elif extension.lower() == 'd' or extension.lower() == 'days':
        return value * 3600 * 24
    else:
        return value
