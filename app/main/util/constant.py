class CARD_TYPE:
    BIG_IMAGE = "bigImage"
    SMALL_IMAGE = "smallImage"
    NESTED_IMAGE = 'nestedImage'
    LIST = [BIG_IMAGE, SMALL_IMAGE, NESTED_IMAGE]

class CARD_TYPE_CODE:
    BIG_IMAGE = 1
    SMALL_IMAGE = 2
    NESTED_IMAGE = 3
    LIST = [BIG_IMAGE, SMALL_IMAGE, NESTED_IMAGE]

def _constant_cls_items(self, cls):
    '''
    get constant class attribute and value dict
    return {'attribute1':0, 'attribute2':1, 'attribute3':2, 'attribute3':3, 'attribute4':4, 'attribute5':5 }
    :param cls: class
    :return: attribute and value dict
    '''
    d_ = {}
    for attribute in cls.__dict__.keys():
        if attribute[:2] != '__':
            value = getattr(cls, attribute)
            if not callable(value):
                d_[attribute] = value
    return d_

# print('debug')