#### 1.创建虚拟环境
```cmd
py -m venv .env
.env\Scripts\activate   # 启用虚拟环境
```
#### 2.安装依赖
```cmd
pip install django
pip install djangorestframework

```
#### 3.创建项目
```cmd
django-admin startproject Scene
```
#### 4.创建应用
```cmd
cd Scene
py manage.py startapp SiteArchive
```
#### 5.创建模型
#### 6.创建序列化器
#### 7.执行数据
```cmd
py manage.py makemigrations SiteArchive
py manage.py migrate
```
#### 8.配置文件settings.py上传目录
```py
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
```
#### 9.配置搜索
```cmd
pip install django-filters
```
#### 10.分页
#### 11.api文档
```cmd
pip install coreapi
```