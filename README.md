cat /etc/issue
 查看当前系统版本
sqlalchemy.exc.InvalidRequestError: Object '<>' is already attached to sessi

from fiat.model.origin_data import db

python 列表的赋值，浅拷贝和深拷贝
以列表的复制为例
"="赋值是达不到复制的效果的,a = b，只是代表他们指向同一片内存，修改a的同时b也会发生变化
赋值操作（包括对象作为参数、返回值）不会开辟新的内存空间，它只是复制了新对象的引用
浅拷贝：浅拷贝会创建新对象，其内容是原对象的引用。
b = a[:]  切片
b = list(a) 工厂函数
b = copy.copy(a)  copy函数
不过浅拷贝只是拷贝了一层，如果a中有嵌套列表，修改嵌套列表的话，浅拷贝的b也会发生变化
深拷贝：
b = copy.deepcopy(a)
拷贝了所有，包含多层嵌套的元素，生成了一个全新的对象
需注意：
1.对于非容器类型，如数字，字符，以及其它“原子”类型，没有拷贝一说。产生的都是原对象的引用。。
2、如果元组变量值包含原子类型对象，即使采用了深拷贝，也只能得到浅拷贝


要复制列表的话，使用切片的方式，b=a[:]
2.
查看变量内存地址
id(a)

后期绑定 ，闭包
ruby列表切片和python 不同，使用a[1,5]


6

ruby中将字符串转化成数组的几种方法
以字符串"games,fun,sports"为例

1.可以使用split(',')转化成数组
"games,fun,sports".split(',') # => ["games", "fun", "sports"]

2.如果是JSON格式的字符串，例如'["games", "fun", "sports"]'
'["games", "fun", "sports"]'.split(',') # =>
 ["[\"games\"", " \"fun\"", " \"sports\"]"]
 不是我们想要的结果
 此时可以使用json库来格式化字符串
只需要
require 'json'
JSON['["games", "fun", "sports"]'] # => ["games", "fun", "sports"]
即可
原文是来自stackoverflow的问题
原文链接https://stackoverflow.com/questions/39337794/how-to-convert-a-string-to-an-array-using-ruby-on-rails


array = array.uniq
uniq method删除所有重复的元素，并保留数组中的所有唯一元素。

vi下查找指定字符串
在命令模式下输入 /

py2neo中的OGM，类似于ORM，意为 Object Graph Mapping，可以实现一个对象和 Node 的关联
利用ogm来生成节点间关系，需要先在出度类中定义比如
ownedBy = RelatedTo("Project")
然后通过自己定义的retrieveId()来获取点
最后通过a.ownedBy.add(b)来生成关系
上传到数据库graph.push(a)

查询所有

利用flask-sqlalchemy多条件查询语句：
OriginalData.query.filter_by(data_type = data_type, original_id = original_id).first()

os.path.relpath(path)
返回真实路径，例如
path=D:\FIAT1224\FIAT_Visual_API\fiat\myapi\..\orig_data\orig-00007
os.path.relpath(path)后即变成
D:\FIAT1224\FIAT_Visual_API\fiat\orig_data\orig-00007

安装 flask-sqlalchemy==2.3.2库时出现unresolved reference SQLALCHEMY
是因为导入包的问题已经由原来的from flask.ext.sqlalchemy import SQLAlchemy
改为from flask_sqlalchemy import SQLAlchemy

use fiat_data_db;使用fiat_data_db数据库
show tables; 显示fiat_data_db中的所有表
select * from original_data; 查询original_data中的所有数据
drop table original_data; 删除original_data表
desc original_data;  查看original_data表结构

关于远程连接126上的mysql失败
sqlalchemy.exc.OperationalError: (pymysql.err.OperationalError) (1045, "Access denied for user 'root'@'10.167.223.152' (using password: YES)") (Background on this error at: http://sqlalche.me/e/e3q8)
原因：是因为root账户只能在本地访问，无法远程连接
解决：新建一个普通账户并把fiat_data_db的权限都赋给它，并且开启远程连接权限
CREATE USER 'fnst'@'localhost' IDENTIFIED BY 'fnst';
grant all on fiat_data_db.* to 'fnst'@'%' identified by 'fnst' with grant option

格式化字符串可以采用%和.format两种方法
print('%s is %d'%('wang',14))
其中.format可以采用位置，关键字，下标作为参数
print("{name} is {age} years old".format(name = "wang",age = 21))
print("{0} is {1} years old".format("wang",21))
print("{1[0]} is {1[1]} years old".format(["wang",21],["li",18]))
