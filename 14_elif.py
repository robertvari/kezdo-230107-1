status = 500


if status == 100:
    print("Status: Continue")
elif status == 200:
    print("Status: OK")
elif status == 300:
    print("Status: Multiple Choices")
elif status == 400:
    print("Status: Bad Request")
elif status == 500:
    print("Status: Internal Server Error")
else:
    print("This status is not handled :(")