import csv

with open('churn.csv') as csvfile:
    next(csvfile)
    data = csv.reader(csvfile, delimiter=',', quotechar='|')

    revenue_per_user = 0.0
    amount_of_users = 0

    mail_check = []
    electronic_check = []
    bank_transfer = []
    credit_card = []

    type_of_contract_for_charn_users = []

    total_charge_of_users_left = 0
    total_charge_of_users_stayed = 0

    clients_months = {"Clients from 0 to 10 months": 0, 'Clients from 10 to 30 months': 0,
                      'Clients from 30 to 50 months': 0, 'Clients from 50 months': 0}

    for row in data:
        internet_service = row[8]
        payment_method = row[17]
        churn = row[20]
        type_of_contract = row[15]
        month = int(row[5])

        total_charges = 0.0
        try:
            total_charges = float(row[19].strip())
        except ValueError:
            pass

        if internet_service != 'No': #1

            amount_of_users += 1
            revenue_per_user += total_charges

            if payment_method == 'Mailed check':  #1 Split these users by different types of payment.
                mail_check.append(row)
            elif payment_method == 'Bank transfer (automatic)':
                bank_transfer.append(row)
            elif payment_method == 'Electronic check':
                electronic_check.append(row)
            elif payment_method == 'Credit card (automatic)':
                credit_card.append(row)

        if churn == 'Yes':  # 3
            total_charge_of_users_left += total_charges
            type_of_contract_for_charn_users.append(type_of_contract)
        else:
            total_charge_of_users_stayed += total_charges

        if month < 10: #4
            clients_months["Clients from 0 to 10 months"] += total_charges
        elif 10 <= month < 30:
            clients_months["Clients from 10 to 30 months"] += total_charges
        elif 30 <= month < 50:
            clients_months["Clients from 30 to 50 months"] += total_charges
        elif month > 50:
            clients_months['Clients from 50 months'] += total_charges


    average_revenue = revenue_per_user / amount_of_users  # 1
    print(average_revenue)
    print(mail_check, electronic_check, bank_transfer, credit_card)


    ration_of_revenue = total_charge_of_users_left / total_charge_of_users_stayed  # 2
    print(ration_of_revenue)

    most_preferred_contract_of_charn_users = max(set(type_of_contract_for_charn_users),
                                                 key=type_of_contract_for_charn_users.count)  # 3
    print(most_preferred_contract_of_charn_users)

    max_contract = max(clients_months, key=clients_months.get)  # 4
    print(max_contract)
