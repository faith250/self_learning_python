def http_error(status):
    match status:
        case 404:
            return"not found"
        case 400:
            return"bad request"
        case 418:
            return "wo swqhuai ni"
        case _:
            return"something is wrong with your internet"
        

http_error(404)
#see calling functions
#case 400|410|414:
#   return "not allowed"