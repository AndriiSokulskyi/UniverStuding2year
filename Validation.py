from datetime import date


def dig_valid(func):
    def func_wrapper(self, num):
        if num != None:
            if (num.isdigit() == False):
                print('It must be only numbers')
                num = 'Incorect'
            res = func(self, num)
            return res
    return func_wrapper


def id_valid(func):
    @dig_valid
    def func_wrapper(self, id):
        if id != None:
            if (len(id) != 8):
                print('It must be ID')
                id = 'Incorect'
            res = func(self, id)
            return res
    return func_wrapper


def alfa_valid(func):
    def func_wrapper(self, alfa):
        if alfa != None:
            if (alfa.isalpha() == False):
                print ('It must be only letterts')
                alfa = 'Incorect'
            res = func(self, alfa)
            return res
    return func_wrapper


def cc_valid(func):
    @alfa_valid
    def func_wrapper(self, country_code):
        if country_code != None:
            if not (country_code.islower() | (
                    len(country_code) < 4)):  # All country codes have max 3 letters( I`ve googled) )
                print('It must be country code (small letters, less then 4)')
                country_code = 'Incorect'
            res = func(self, country_code)
            return res
    return func_wrapper


def pn_valid(func):
    def func_wrapper(self, passport_no):
        if passport_no != None:
            if not((len(passport_no) == 8) | passport_no[0:2].isupper() | passport_no[2:8].isdigit()):
                print('It must be passport № (First two - big letters, next 6 digits)')
                passport_no = 'Incorect'
            res = func(self, passport_no)
            return res
    return func_wrapper


def date_valid(func):
    def func_wrapper(self, date, date2):
        if date != None:
            if (len(date) == 10) & date[0:4].isdigit() & date[5:7].isdigit() & date[8:10].isdigit() & (date[4] == '-') & (date[7] == '-'):
                if (0 < int(date[5:7]) < 13) & (0 < int(date[8:10]) < 32):
                    if (date[5:7] == '02') & (int(date[8:10]) > 29):
                        print('Feb has max 29 days.')
                        date = 'Incorect'
                    elif (date[5:7] == '02') & (int(date[8:10]) > 28) & (int(date[0:4])%4 != 0):
                        print('Feb has 28 days, when year is not intercalary.')
                        date = 'Incorect'
                    elif ( date[5:7] == '04' or date[5:7] == '06' or date[5:7] == '09' or date[5:7] =='11' ) & ( int(date[8:10]) > 30 ):
                        print('Apl, Jun, Sep and Nov have max 29 days.')
                        date = 'Incorect'
                else:
                    print('Month has max 31 days and year has max 12 month')
                    date = 'Incorect'
            else:
                print('It must be date (xx.xx.xxxx)')
                date = 'Incorect'
            res = func(self, date, date2)
            return res
    return func_wrapper


def birth_valid(func):
    def func_wrapper(self, date_of_birth, date2):
        if date_of_birth != None:
            if (str(date.today()) < date_of_birth) | (date_of_birth < '1900-01-01'):
                print('This person is unborned or dead')
                date_of_birth = 'Incorect'
            res = func(self, date_of_birth, date2)
            return res
    return func_wrapper


def issue_valid(func):
    def func_wrapper(self, date_of_issue, date_of_birth):
        if date_of_issue != None:
            if (str(date.today()) < date_of_issue) | (date_of_issue < date_of_birth):
                print('This person can`t get forirgn passport before birth or in future')
                date_of_issue = 'Incorect'
            res = func(self, date_of_issue, date_of_birth)
            return res
    return func_wrapper


def expire_valid(func):
    def func_wrapper(self, date_of_expire, date_of_issue):
        if (date_of_expire!= None):
            if date_of_expire < str(date_of_issue):
                print('Foreign passport can`t be expired before getting')
                date_of_expire = 'Incorect'
            res = func(self, date_of_expire, date_of_issue)
            return res
    return func_wrapper


def txt_valid(func):
    @file_existing
    def func_wrapper(txt, mode):
        if not (txt.endswith('.txt')):
            raise ValueError('It is not txt file.')
        res = func(txt, mode)
        return res
    return func_wrapper


def file_existing(func):
    def func_wrapper(file, mode):
        try:
            f = open(file, mode)
        except IOError:
            raise IOError('File don`t exist.')
        res = func(file, mode)
        return res
    return func_wrapper