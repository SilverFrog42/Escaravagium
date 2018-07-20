def input_data():
    send_user = input("Who would you like to send money to?: ")
    send_money = int(input("How much would you like to send?: "))
    print("Processing...")
    return send_user + str(send_money)