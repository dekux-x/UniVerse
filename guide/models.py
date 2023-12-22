from django.db import models
from django.contrib.auth.models import User


class University(models.Model):
    name = models.CharField(max_length=200)
    address = models.JSONField()
    number = models.CharField(max_length=20)
    site = models.CharField(max_length=100)
    type = models.CharField(max_length=20)
    description = models.TextField()
    dormitary = models.BooleanField()

    def __str__(self):
        return self.name

class Faculty(models.Model):
    univ_id = models.ForeignKey(University, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    count_of_programs = models.PositiveSmallIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name

class Grant(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=200)
    amount = models.IntegerField()
    year = models.PositiveSmallIntegerField()
    max = models.PositiveSmallIntegerField()
    min = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.code

class Program(models.Model):
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    grant_code = models.ForeignKey(Grant, on_delete=models.SET_DEFAULT, default=None)
    name = models.CharField(max_length=200)
    degree = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.CharField(max_length=100)
    requirements = models.JSONField(default= dict)

    def __str__(self):
        return self.name

class FavoriteUnivList(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    list = models.JSONField(default=dict)

class FavoriteProgList(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    list = models.JSONField(default=dict)

class GrantsList():
    grants_list = [
        {"Код": "В001", "max": "127", "min": "98"},
        {"Код": "В002", "max": "106", "min": "75"},
        {"Код": "В003", "max": "125", "min": "98"},
        {"Код": "В005", "max": "124", "min": "120"},
        {"Код": "В006", "max": "123", "min": "119"},
        {"Код": "В009", "max": "136", "min": "125"},
        {"Код": "В010", "max": "136", "min": "112"},
        {"Код": "В011", "max": "129", "min": "78"},
        {"Код": "В012", "max": "129", "min": "107"},
        {"Код": "В013", "max": "133", "min": "95"},
        {"Код": "В014", "max": "123", "min": "100"},
        {"Код": "В015", "max": "134", "min": "104"},
        {"Код": "В016", "max": "132", "min": "118"},
        {"Код": "В017", "max": "127", "min": "100"},
        {"Код": "В018", "max": "139", "min": "122"},
        {"Код": "В019", "max": "97", "min": "75"},
        {"Код": "В020", "max": "130", "min": "90"},
        {"Код": "В021", "max": "120", "min": "115"},
        {"Код": "В027", "max": "122", "min": "116"},
        {"Код": "В028", "max": "123", "min": "117"},
        {"Код": "В029", "max": "122", "min": "118"},
        {"Код": "В030", "max": "123", "min": "113"},
        {"Код": "В031", "max": "125", "min": "119"},
        {"Код": "В032", "max": "102", "min": "89"},
        {"Код": "В033", "max": "125", "min": "117"},
        {"Код": "В034", "max": "128", "min": "99"},
        {"Код": "В134", "max": "124", "min": "93"},
        {"Код": "В035", "max": "125", "min": "113"},
        {"Код": "В135", "max": "133", "min": "116"},
        {"Код": "В036", "max": "137", "min": "118"},
        {"Код": "В037", "max": "132", "min": "115"},
        {"Код": "В038", "max": "120", "min": "103"},
        {"Код": "В039", "max": "117", "min": "114"},
        {"Код": "В040", "max": "126", "min": "115"},
        {"Код": "В140", "max": "137", "min": "126"},
        {"Код": "В041", "max": "136", "min": "97"},
        {"Код": "В042", "max": "125", "min": "120"},
        {"Код": "В043", "max": "115", "min": "104"},
        {"Код": "В044", "max": "137", "min": "119"},
        {"Код": "В045", "max": "136", "min": "113"},
        {"Код": "В145", "max": "127", "min": "113"},
        {"Код": "В046", "max": "139", "min": "113"},
        {"Код": "В047", "max": "138", "min": "111"},
        {"Код": "В048", "max": "119", "min": "108"},
        {"Код": "В049", "max": "134", "min": "116"},
        {"Код": "В050", "max": "135", "min": "80"},
        {"Код": "В051", "max": "120", "min": "73"},
        {"Код": "В052", "max": "124", "min": "71"},
        {"Код": "В053", "max": "134", "min": "68"},
        {"Код": "В054", "max": "131", "min": "69"},
        {"Код": "В055", "max": "137", "min": "96"},
        {"Код": "В056", "max": "119", "min": "50"},
        {"Код": "В057", "max": "138", "min": "96"},
        {"Код": "В058", "max": "134", "min": "62"},
        {"Код": "В059", "max": "135", "min": "68"},
        {"Код": "В060", "max": "136", "min": "50"},
        {"Код": "В061", "max": "135", "min": "50"},
        {"Код": "В062", "max": "136", "min": "58"},
        {"Код": "В162", "max": "32", "min": "27"},
        {"Код": "В063", "max": "138", "min": "61"},
        {"Код": "В064", "max": "130", "min": "50"},
        {"Код": "В065", "max": "132", "min": "50"},
        {"Код": "В066", "max": "114", "min": "72"},
        {"Код": "В067", "max": "129", "min": "74"},
        {"Код": "В167", "max": "131", "min": "90"},
        {"Код": "В165", "max": "102", "min": "50"},
        {"Код": "В166", "max": "86", "min": "50"},
        {"Код": "В068", "max": "100", "min": "52"},
        {"Код": "В069", "max": "73", "min": "50"},
        {"Код": "В070", "max": "94", "min": "50"},
        {"Код": "В071", "max": "139", "min": "50"},
        {"Код": "В171", "max": "29", "min": "0"},
        {"Код": "В271", "max": "44", "min": "25"},
        {"Код": "В072", "max": "119", "min": "69"},
        {"Код": "В073", "max": "125", "min": "111"},
        {"Код": "В173", "max": "0", "min": "0"},
        {"Код": "В175", "max": "67", "min": "50"},
        {"Код": "В074", "max": "136", "min": "52"},
        {"Код": "В176", "max": "76", "min": "54"},
        {"Код": "В075", "max": "113", "min": "85"},
        {"Код": "В076", "max": "129", "min": "66"},
        {"Код": "В077", "max": "106", "min": "50"},
        {"Код": "В078", "max": "72", "min": "50"},
        {"Код": "В079", "max": "92", "min": "69"},
        {"Код": "В080", "max": "78", "min": "50"},
        {"Код": "В082", "max": "81", "min": "50"},
        {"Код": "В183", "max": "85", "min": "50"},
        {"Код": "В083", "max": "123", "min": "50"},
        {"Код": "В091", "max": "138", "min": "104"},
        {"Код": "В092", "max": "123", "min": "115"},
        {"Код": "В093", "max": "136", "min": "101"},
        {"Код": "В094", "max": "115", "min": "67"},
        {"Код": "В095", "max": "131", "min": "108"},
        {"Код": "В090", "max": "104", "min": "74"},
        ]

    def get_list(self):
        return self.grants_list
    
    def get_by_code(self, code: str):
        answer = None
        for grant in self.grants_list:
            if code == grant["Код"]:
                answer = grant
                break
        return answer


