from datetime import date
cc_dictio={ 0 : 'ukr', 1 : 'isr', 2 :'pol', 3 :'swz', 4 : 'itl'}


class Validation:

    @staticmethod
    def dig_valid(num):
        if (num != None) and (num != "None"):
            if (num.isdigit() == False):
                print ('It must be only numbers')
                return "None"
            else:
                return num

    @staticmethod
    def id_valid(id):
        if (id != None) and (id != "None"):
            id = Validation.dig_valid(id)
            if (len(id) == 8):
                return id
            else:
                print('It must be ID')
                return "None"

    @staticmethod
    def alfa_valid(alfa):
        if (alfa != None) and (alfa != "None"):
            if (alfa.isalpha() == False):
                print ('It must be only letterts')
                return "None"
            else:
                return alfa

    @staticmethod
    def cc_valid(country_code):
        if (country_code != None) and (country_code != "None"):
            for i in range(len(cc_dictio)):
                if (country_code == cc_dictio[i]):
                    return Validation.alfa_valid(country_code)
            print('It must be country code (small letters, less then 4)')
            return "None"

    @staticmethod
    def pn_valid(passport_no):
        if (passport_no != None) and (passport_no != "None"):
            if (len(passport_no) == 8) & passport_no[0:2].isupper() & passport_no[2:8].isdigit():
                return passport_no
            else:
                print('It must be passport № (First two - big letters, next 6 digits)')
                return "None"

    @staticmethod
    def date_valid(date):
        if (date != None) and (date != "None"):
            if (len(date) == 10) & date[0:4].isdigit() & date[5:7].isdigit() & date[8:10].isdigit() & (date[4] == '-') & (date[7] == '-'):
                if (0 < int(date[5:7]) < 13) & (0 < int(date[8:10]) < 32):
                    if (date[5:7] == '02') & (int(date[8:10]) > 29):
                        print('Feb has max 29 days.')
                        return "None"
                    elif (date[5:7] == '02') & (int(date[8:10]) > 28) & (int(date[0:4])%4 != 0):
                        print('Feb has 28 days, when year is not intercalary.')
                        return "None"
                    elif ( date[5:7] == '04' or date[5:7] == '06' or date[5:7] == '09' or date[5:7] =='11' ) & ( int(date[8:10]) > 30 ):
                        print('Apl, Jun, Sep and Nov have max 29 days.')
                        return "None"
                    else:
                        return date
                else:
                    print('Month has max 31 days and year has max 12 month')
                    return "None"
            else:
                print('It must be date (xx.xx.xxxx)')
                return "None"

    @staticmethod
    def birth_valid(date_of_birth):
        if (date_of_birth != None) and (date_of_birth != "None"):
            if str(date.today()) > date_of_birth > '1900-01-01':
                return Validation.date_valid(date_of_birth)
            else:
                print('This person is unborned or dead')
                return "None"

    @staticmethod
    def issue_valid(date_of_issue, date_of_birth):
        if ((date_of_issue != None) and (date_of_issue != "None")) & ((date_of_birth != None) and (date_of_birth != "None")):
            if str(date.today()) > date_of_issue > date_of_birth:
                return Validation.date_valid(date_of_issue)
            else:
                print('This person can`t get forirgn passport before birth or in future')
                return "None"

    @staticmethod
    def expire_valid(date_of_expire, date_of_issue):
        if  ((date_of_expire != None) and (date_of_expire != "None")) & ((date_of_issue != None) and (date_of_issue != "None")):
            if date_of_expire > date_of_issue:
                return Validation.date_valid(date_of_expire)
            else:
                print('Foreign passport can`t be expired before getting')
                return "None"

    @staticmethod
    def txt_valid(txt):
        while not(txt.endswith('.txt')):
            print('It is not txt file.')
            txt = input('Input "name of file".txt')
        return txt

    @staticmethod
    def file_existing(file, mode = "r"):
        while True:
            try:
                f = open(Validation().txt_valid(file), mode)
            except IOError:
                print('File don`t exist.')
                file = input('Input name of file that exists: ')
            else:
                return f