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
