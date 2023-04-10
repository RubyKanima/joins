import logging

class Joins():

    def __init__(self, left, right, attr) -> list:
        self.left = left    
        self.right = right
        self.attr = attr

    def _left_join(left, right):
        return [each for each in left if each not in right]

    def _right_join(left, right):
        return [each for each in right if each not in left]

    def _inner_join(self, left, right):
        return [each for each in left if each in right]
    
    def _outer_join(self, left, right):
        return self._left_join(left,right).extend(self._right_join(self, left, right))
    
    def _inner_join_on(left, right, attr, only_attr = False) -> list:
        if not isinstance(left, type(right)):
            logging.error(f"TypeError: {type(left)} does not equal {type(right)}")
            raise TypeError
        try:
            if isinstance(left[0], type(right[0])):
                _type = type(left[0])
            else:
                raise TypeError
            if only_attr:
                if _type == list | dict:
                    return [getattr(each, attr) for each in left for other in right if each[attr] == other[attr]]
                return [getattr(each, attr) for each in left for other in right if getattr(each, attr) == getattr(other, attr)]
            else:
                if _type == list | dict:
                    return [[each, other] for each in left for other in right if each[attr] == other[attr]]
                return [[each, other] for each in left for other in right if getattr(each, attr) == getattr(other, attr)]
        except AttributeError:
            logging.error(f"Attribute {attr} is not in {left} or {right}")
        except ValueError:
            logging.error(f"{attr} does not fit {_type}")