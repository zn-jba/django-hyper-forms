def unpack(input_tuple):
    items = []
    for element in input_tuple:
        if isinstance(element, str):
            items.append(element)
        else:
            for ele in element:
                items.append(ele)
    return tuple(items)
