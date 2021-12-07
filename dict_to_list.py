
"""
Дан словарь с разной степенью вложенности. На нижнем уровне обязательно находится число.
Нужно написать функцию, которая будет генерировать пары (ключи, соединенные через точку; значение).

Например, из словаря:
a = {
   'b' : 4,
   'c' : {
       'd': 3,
       'e': 5,
       'x':{'y':10},
    }
}


Должно получиться:
[
  ('b', 4),
  ('c.d', 3),
  ('c.e', 5),
  ('c.x.y', 10)
]
"""


def compact_dict(tree_dict, parent_key=''):
    for k, v in tree_dict.items():
        if isinstance(v, dict):
            yield from compact_dict(v, parent_key=parent_key + k + '.')
        else:
            yield parent_key + k, v


assert list(compact_dict(tree_dict={
    'b': 4,
    'c': {
       'd': 3,
       'e': 5,
       'x': {'y': 10},
    }
})) == [
  ('b', 4),
  ('c.d', 3),
  ('c.e', 5),
  ('c.x.y', 10)
]
