#列表支持多种元素同时使用
mix=['何时锦','hahahah',123]
print(mix)
#在列表中末尾添加一个元素
#用append（）方法
mix.append('crazy')
print(mix)
#但是append只能传递一个参数
#要加入多个元素，要用extend
#extend传递的参数为列表
mix.extend(['alex','hahahaaa'])
print(mix)
#准确插入用insert
mix.insert(1,'alice')
print(mix)
#insert要传递两个参数，插入的位置和插入的元素
#访问列表用索引，索引从0开始
print(mix[0])

mix_1=mix

