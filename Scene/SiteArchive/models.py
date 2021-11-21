from django.db import models

# Create your models here.
class Site(models.Model):
    # 局点信息
    site_name = models.CharField(verbose_name='局点名称',max_length=20,help_text='局点名称')
    site_region = models.CharField(verbose_name='所属区域',max_length=20,default=None,help_text='所属区域')
    site_type = models.CharField(verbose_name='局点类型',max_length=20,default=None,help_text='局点类型')
    cus_info = models.CharField(verbose_name='客户信息',max_length=200,default=None,help_text='客户信息')
    deploy_plan = models.CharField(verbose_name='部署方案',max_length=200,help_text='部署方案')
    hardware_config = models.CharField(verbose_name='硬件配置',max_length=200,default=None,help_text='硬件配置')
    osdb_version =  models.CharField(verbose_name='OS/DB版本',max_length=200,default=None,help_text='OS/DB版本')
    product_version = models.CharField(verbose_name='产品版本',max_length=20,help_text='产品版本')
    component_info = models.CharField(verbose_name='组件信息',max_length=200,help_text='组件信息')
    peripheral_docking = models.CharField(verbose_name='周边对接',max_length=200,default=None,help_text='周边对接')
    site_remarks = models.CharField(verbose_name='备注',max_length=200,default=None,help_text='备注')

    def __str__(self):
        return self.site_name

class Networking(models.Model):
    # 组网信息
    site_name = models.ForeignKey(Site,verbose_name='局点名称',on_delete=models.CASCADE,help_text='局点名称')
    site_networking = models.FileField(upload_to='Networking/',verbose_name='组网信息',default=None,help_text='组网信息')
    device_config = models.FileField(upload_to='Networking/',verbose_name='设备配置',default=None,help_text='设备配置')
    manage_scale = models.CharField(verbose_name='管理规模',max_length=200,default=None,help_text='管理规模')

class Feature(models.Model):
    # 关键特征
    site_name = models.ForeignKey(Site,verbose_name='局点名称',on_delete=models.CASCADE,help_text='局点名称')
    key_feature = models.CharField(verbose_name='关键特征',max_length=200,help_text='关键特征')

class Operation(models.Model):
    # 运维活动
    site_name = models.ForeignKey(Site,verbose_name='局点名称',on_delete=models.CASCADE,help_text='局点名称')
    active_name = models.CharField(verbose_name='活动名称',max_length=20,default=None,help_text='活动名称')
    operation_claim = models.CharField(verbose_name='运维诉求',max_length=200,default=None,help_text='运维诉求')
    operation_benefit = models.CharField(verbose_name='价值点',max_length=200,default=None,help_text='价值点')

    def __str__(self):
        return self.active_name

class Operaterole(models.Model):
    # 活动角色
    active_name = models.ForeignKey(Operation,verbose_name='活动名称',on_delete=models.CASCADE,help_text='活动名称')
    role_name = models.CharField(verbose_name='角色名称',max_length=20,help_text='角色名称')

    def __str__(self):
        return self.role_name

class Operatedetail(models.Model):
    # 活动详情
    active_name = models.ForeignKey(Operation,verbose_name='活动名称',on_delete=models.CASCADE,help_text='活动名称')
    role_name = models.ForeignKey(Operaterole,verbose_name='角色名称',on_delete=models.CASCADE,help_text='角色名称')
    active_detail = models.CharField(verbose_name='活动详情',max_length=200,default=None,help_text='活动详情')

    def __str__(self):
        return self.active_detail

class Require(models.Model):
    # 需求
    site_name = models.ForeignKey(Site,verbose_name='局点名称',on_delete=models.CASCADE,help_text='局点名称')
    require_name = models.CharField(verbose_name='需求名称',max_length=20,default=None,help_text='需求名称')
    require_detail = models.CharField(verbose_name='需求详情',max_length=200,default=None,help_text='需求详情')
    require_proposer = models.CharField(verbose_name='提出人',max_length=20,default=None,help_text='提出人')

class Onlineissue(models.Model):
    # 网上问题
    site_name = models.ForeignKey(Site,verbose_name='局点名称',on_delete=models.CASCADE,help_text='局点名称')
    issue_name= models.CharField(verbose_name='问题名称',max_length=20,default=None,help_text='问题名称')
    issue_detail = models.CharField(verbose_name='问题详情',max_length=200,default=None,help_text='问题详情')
    issue_proposer = models.CharField(verbose_name='提出人',max_length=20,default=None,help_text='提出人')
    issue_owner = models.CharField(verbose_name='责任人',max_length=20,default=None,help_text='责任人')

class Travelreport(models.Model):
    # 出差报告
    site_name = models.ForeignKey(Site,verbose_name='局点名称',on_delete=models.CASCADE,help_text='局点名称')
    report_file = models.FileField(upload_to='Travelreport/',verbose_name='报告文件',default=None,help_text='报告文件')
    report_proposer = models.CharField(verbose_name='提交人',max_length=20,default=None,help_text='提交人')

