class Date:

    nums_list = []
    day = 0
    month = 0
    year = 0

    def __init__(self, users_str):
        self.date_str = users_str

    @classmethod
    def to_num(cls, obj):
        cls.nums_list = obj.date_str.split('-')
        for i in range(3):
            if (str(cls.nums_list[i]))[0] == '0':
                cls.nums_list[i] = int(cls.nums_list[i][1:])
            cls.nums_list[i] = int(cls.nums_list[i])
        if cls.is_valid(cls.nums_list):
            cls.day, cls.month, cls.year = map(int, cls.nums_list)
            return cls.day, cls.month, cls.year
        else:
            print('Your date is incorrect! PLease, check it and retry')

    @staticmethod
    def is_valid(date):
        days_leap_year = {29: 2,
                          30: [4, 6, 9, 11],
                          31: [1, 3, 5, 7, 8, 10, 12]}
        days_non_leap_year = {28: 2,
                              30: [4, 6, 9, 11],
                              31: [1, 3, 5, 7, 8, 10, 12]}
        if 1 <= date[1] <= 12:  # if num of month is valid
            if date[2] % 4 == 0:  # if year is leap
                your_dict = days_leap_year
            else:
                your_dict = days_non_leap_year
            for key, value in your_dict.items():
                if type(value) == dict:
                    if date[1] in value:
                        if date[0] <= key:
                            return True
                        else:
                            return False
                else:
                    if date[1] == value:
                        if date[0] <= key:
                            return True
                        else:
                            return False
        else:  # if num of month is not valid
            return False


date_1 = Date('02-02-2000')
print(date_1.to_num(date_1))

date_2 = Date('29-02-2003')
print(date_2.to_num(date_2))
