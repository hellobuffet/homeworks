# 1.	類別繼承的練習-employee
# 有一小公司，其人事薪資的制度如下：
# 公司每個員工皆有姓名、性別、到職日、電話和住址等基本資料。
# 一般職員只有本薪；一級主管則另有本薪、午餐津貼、交通津貼和職務加給；二級主管則有本薪、午餐津貼和職務加給。午餐津貼為1800元，交通津貼為2000元，職務加給一級主管為5000元，二級主管為3000元。
# 每個員工皆有可能加班，加班費為本薪除以240乘以1.5倍再乘以加班時數。
# 在main()中產生六個實例分別為一級主管、二級主管及一般職員且分有加班及無加班兩種(資料直接透過建構子hard code在程式中)，並列印其基本資料及當月薪資。

class employee:
    def __init__(self, name='noName', sex='noSex', work_date='noWork_date', phone='noPhone', home_access='noAccess'):
        self.name = name
        self.sex = sex
        self.work_date = work_date
        self.phone = phone
        self.home_access = home_access
        self.salary = 0

    def __str__(self):
        return (
            'Name:{}, Sex:{}, Work_date:{}, Phone:{}, Access:{}, salary:{}'.format(self.name, self.sex, self.work_date,
                                                                                   self.phone,
                                                                                   self.home_access, self.salary))

    def ordinary(self, salary, overtime):
        self.salary = salary+((salary / 240) * 1.5 * overtime)

    def Primary_supervisor(self, salary):
        self.salary = salary+(1800 + 2000 + 5000)

    def Secondary_supervisor(self, salary):
        self.salary = salary+ (1800 + 3000)


buffet = employee('hellobuffet', '男', '2018/01/01', '0972126115', '羅德島')
buffet.ordinary(18000, 0)
buffet.Primary_supervisor(18000)

print(buffet)
