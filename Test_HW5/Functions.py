import math


def task_1(list1, list2):
    return list(set(list1) & set(list2))


def task_2(sentence):
    return sentence.count('a')


def task_3(num):
    x = math.log(num, 3)
    return int(x) == x


def task_4(num):
    while True:
        digits_count = sum(int(digit) for digit in str(num))
        if digits_count <= 9:
            return digits_count
        num = digits_count


def task_5(n):
    a = 0
    for i in n:
        if i == 0:
            n.remove(i)
            n.append(0)
        a += 1
    return n


def task_6(num):
    if len(num) < 2:
        return False
    dif = num[1] + num[2]
    ind = 1
    while ind < len(num - 1):
        if num(ind+1) != num[ind] + dif:
            return False
        ind += 1
    return True


def task_7(lst):
    result = []
    for i in lst:
        counter = 0
        n = i
        for j in lst:
            if n == j:
                counter += 1
        if counter == 1:
            result.append(n)
    return result


def task_8(lst):
    good_lst = []
    counter = int(lst[0])
    n = len(lst)-1
    for i in range(counter, lst[n]+1):
        good_lst.append(counter)
        counter += 1
    return list(set(lst) ^ set(good_lst))


def task_9(lst):
    counter = 0
    for i in range(0, len(lst)-1):
        if not isinstance(lst[i], tuple):
            counter += 1
    return counter


def task_10(text):
    return text[::-1]


def task_11(minute):
    time_hours = minute // 60
    time_minute = minute % 60
    return str(time_hours) + ':' + str(time_minute)


def task_12(text):
    result = ''
    for i in text:
        if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122 or ord(i) == 32:
            result += i
    result = result.split()
    counter = result[0]
    for i in result:
        if len(i) > len(counter):
            counter = i
    return counter


def task_13(text):
    result = ' '
    text = text.split()
    text = text[::-1]
    result = result.join(text)
    return result


def task_14(n):
    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib


def task_15(lst):
    return [i for i in lst if i % 2 == 0]


def task_16(numb):
    res = 0
    for i in range(1, numb+1):
        res += i
    return res


def task_17(numb):
    res = 1
    for i in range(1, numb + 1):
        res = res * i
    return res


def task_18(text):
    #res = [chr((ord(i)+1)) for i in text if True]
    res = ''
    for i in text:
        res += chr((ord(i)+1))
    return res


def test(lst):
    small = lst[0]
    small_index = 0
    for i in range(1, len(lst)):
        if lst[i] < small:
            small = lst[i]
            small_index = i
    return small_index


def task_19(data):
    lst = [ord(i) for i in data]
    newels = []
    for i in range(len(lst)):
        small = test(lst)
        newels.append(lst.pop(small))
    return ''.join(map(str, [chr(i) for i in newels]))


def task_20(num_1, num_2):
    if num_2 > num_1:
        return True
    return False
