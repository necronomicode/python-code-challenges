# Link: https://www.codewars.com/kata/51ba717bb08c1cd60f00002f

def solution(args):
    result = []
    i = 0

    while i < len(args):
        start = args[i]

        while i+1 < len(args) and args[i] == args[i+1] - 1:
            i += 1

        end = args[i]

        if end - start >= 2:
            result.append(f"{start}-{end}")
        
        elif end - start == 1:
            result.extend([str(start), str(end)])

        else:
            result.append(str(start))

        i += 1

    return ",".join(result)