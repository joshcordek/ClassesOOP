class Customer:
    def __init__(self, customerid, name, address, email, phone, member_status):
        self._customerid = customerid
        self._name = name
        self._address = address
        self._email = email
        self._phone = phone
        self._member_status = member_status

    def get_customerid(self):
        return self._customerid

    def get_name(self):
        return self._name

    def get_address(self):
        return self._address

    def get_email(self):
        return self._email

    def get_phone(self):
        return self._phone

    def get_member_status(self):
        return self._member_status


class Transaction:
    def __init__(self, date, item_name, cost, customerid):
        self._date = date
        self._item_name = item_name
        self._cost = cost
        self._customerid = customerid

    def get_date(self):
        return self._date

    def get_item_name(self):
        return self._item_name

    def get_cost(self):
        return self._cost

    def get_customerid(self):
        return self._customerid
