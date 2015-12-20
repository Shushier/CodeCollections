# 001  dict.get(key, []).insert(0, value)错误
d = dict()
listx = [1, 2, 3]
d['a'] = d.get('a', []).insert(0, listx)
print(d) 
# 输出结果为  {'a': None}
# 原因是list的insert方法的返回值为None而不是更新后的list
# 因之，list是不能进行连续插入操作的，如 
# d.get('a', []).insert(0, listx).insert(0, listx)，会报错
# AttributeError: 'NoneType' object has no attribute 'insert'

# 002 python 3.x map()函数被设计为lazy function，返回值为一个迭代器对象，用法上需要注意
# print(map())的结果为map()的内存对象索引<map object at 0x0000000003B50C18>，并没有直接可用的值
# 使用值需要这样 
for item in map(None, *items):
    pass

# 003 python类内部调用自己的方法必须加self
class demo:
    def fa(self):
        return 'aa'
    def fb(self):
        return self.fa()    




