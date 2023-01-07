status = 100

match status:
    case 100:
        print("Status: Continue")
    case 200:
        print("Status: OK")
    case 300:
        print("Status: Multiple Choices")
    case 400:
        print("Status: Bad Request")
    case 500:
        print("Status: Internal Server Error")
    case _:
        print("This status is not handled :(")