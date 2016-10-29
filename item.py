class DirectoryItem:

    def __init__(self, name, last_name, address, mobile_phone, home_phone):
        self.name = name
        self.last_name = last_name
        self.address = address
        self.mobile_phone = mobile_phone
        self.home_phone = home_phone

    def __str__(self):
        return str(self.name + ', ' + self.last_name
                   + ', ' + self.address + ', ' + str(self.mobile_phone)
                   + ', ' + str(self.home_phone))

    def __repr__(self):
        return str(':::' + self.name + ',' + self.last_name
                   + ',' + self.address + ',' + str(self.mobile_phone)
                   + ',' + str(self.home_phone) + ':::')
