def snail(snail_map):
    result = []

    while snail_map:
        result.extend(snail_map.pop(0))

        for row in snail_map:
            result.append(row.pop())

        if snail_map:
            result.extend(snail_map.pop()[::-1])
        
        for row in snail_map[::-1]:
            result.append(row.pop(0))

    return result

        
