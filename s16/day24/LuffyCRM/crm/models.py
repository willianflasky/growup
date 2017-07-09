from django.db import models
# Create your models here.


class Source(models.Model):
    name = models.CharField(max_length=64, unique=True)


class Tag(models.Model):
    name = models.CharField(max_length=64, unique=True)


class Customer(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    qq = models.CharField(max_length=64, unique=True, blank=True, null=True)
    weixin = models.CharField(max_length=64, unique=True, blank=True, null=True)
    phone = models.BigIntegerField(unique=True, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    source = models.ForeignKey('Source')
    referral_from = models.ForeignKey('Account', blank=True, null=True)
    consult_courses = models.ManyToManyField('Course')
    content = models.TextField("首次咨询内容/客户详情")
    status_choices = (
        (0, "已报名"),
        (1, "已退费"),
        (2, "未报名"),
    )
    status = models.SmallIntegerField(choices=status_choices, default=2)
    tags = models.ManyToManyField('Tag', blank=True)
    consultant = models.ForeignKey('Account')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class PaymentRecord(models.Model):
    """缴费记录"""
    customer = models.ForeignKey('Customer')
    class_list = models.ForeignKey('ClassList')
    payment_method_choices = (
        (0, '现金'),
        (1, '微信'),
        (2, '支付宝'),
        (3, '刷卡'),
        (4, '学生贷款'),
    )
    payment_method = models.SmallIntegerField(choices=payment_method_choices)

    payment_type_choices = (
        (0, '报名费'),
        (1, '学费'),
        (2, '退费'),
    )
    payment_type = models.SmallIntegerField(choices=payment_type_choices)
    account = models.ForeignKey('Account')
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)


class CustomerFollowup(models.Model):
    """学员跟踪表"""
    customer = models.ForeignKey('Customer')
    content = models.TextField()
    consultant = models.ForeignKey('Account')
    date = models.DateTimeField(auto_now_add=True)
    status_choices = (
        (0, '决不考虑'),
        (1, '短期内不考虑'),
        (2, '已在其它机构报名'),
        (3, '2周内报名'),
        (4, '已报名'),
        (5, '已试听'),
    )
    status = models.IntegerField(choices=status_choices)


class Course(models.Model):
    """班级"""
    name = models.CharField(max_length=128, unique=True)
    period = models.IntegerField("周期(月)")
    price = models.IntegerField()
    outline = models.TextField()

    def __str__(self):
        return self.name


class Branch(models.Model):
    """校区"""
    name = models.CharField(max_length=64, unique=True)


class ClassList(models.Model):
    """班级"""
    course = models.ForeignKey('Course')
    branch = models.ForeignKey('Branch')
    semester = models.IntegerField("学期")
    class_type_choices = (
        (0, '周末'),
        (1, '脱产'),
        (2, '网络'),
    )
    class_type = models.SmallIntegerField(choices=class_type_choices)

    max_students_num = models.IntegerField(default=80)
    teacher = models.ManyToManyField('Account')
    start_date = models.DateField("开班日期")
    end_date = models.DateField("结业日期", blank=True, null=True)

    def __str__(self):
        return "%s(%s)" % (self.course, self.semester)

    class Meta:
        """联合唯一"""
        unique_together = ('course', 'branch', 'semester', 'class_type')


class CourseRecord(models.Model):
    """上课记录"""
    class_list = models.ForeignKey('ClassList')
    day_num = models.IntegerField("节次")
    name = models.CharField(max_length=128)
    teacher = models.ForeignKey('Account')
    has_homework = models.BooleanField(default=True)
    homework_title = models.CharField(max_length=128, blank=True, null=True)
    homework_requirement = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s(%s)-%s" % (self.class_list, self.day_num, self.name)

    class Meta:
        unique_together = ('class_list', 'day_num')


class StudyRecord(models.Model):
    """学习记录"""
    student = models.ForeignKey('Account')
    course_record = models.ForeignKey('CourseRecord')
    score_choices = (
        (100, 'A+'),
        (90, 'A'),
        (85, 'B+'),
        (70, 'B'),
        (65, 'C+'),
        (60, 'C'),
        (40, 'C-'),
        (-50, 'D'),
        (0, 'N/A'),
        (-100, 'COPY'),
    )

    score = models.IntegerField(choices=score_choices)

    show_status_choices = (
        (0, '正常'),
        (1, '迟到'),
        (2, '缺勤'),
        (3, 'N/A'),
    )
    show_status = models.IntegerField(choices=show_status_choices)
    comment = models.TextField('批注', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'course_record')


class Enrollment(models.Model):
    """已经报名课程"""
    account = models.ForeignKey('Account')
    class_list = models.ForeignKey('ClassList')
    date = models.DateTimeField(auto_now_add=True)


class Contract(models.Model):
    """合同"""
    name = models.CharField(max_length=128, unique=True)
    content = models.TextField('合同内容')
    date = models.DateField(auto_now_add=True)


class Role(models.Model):
    """角色"""
    name = models.CharField(max_length=64, unique=True)
    menus = models.ManyToManyField('Menu', blank=True, null=True)

    def __str__(self):
        return self.name


class Menu(models.Model):
    """一级菜单"""
    name = models.CharField(max_length=64)
    url_type_choices = (
        (0, 'absolute'),
        (1, 'relative'),
    )

    url_type = models.PositiveIntegerField(choices=url_type_choices, default=1)
    url = models.CharField(max_length=128)
    order = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('url', 'url_type')


class SubMenu(models.Model):
    """二级菜单"""
    menu = models.ForeignKey('Menu')
    name = models.CharField(max_length=64)
    url_type_choices = (
        (0, 'absolute'),
        (1, 'relative'),
    )
    url_type = models.PositiveIntegerField(choices=url_type_choices, default=1)
    url = models.CharField(max_length=128)
    order = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('url', 'url_type')


class Account(models.Model):
    """用户表"""
    models.OneToOneField('User')


