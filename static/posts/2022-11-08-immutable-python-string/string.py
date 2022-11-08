from time import time

def merge_using_string_operation():
    string = ''
    start = time()
    for _i in range(100000):
        string += 'string '
    end = time()
    return end - start

def merge_using_list_append():
    string = ''
    start = time()
    string_buf = []
    for _i in range(100000):
        string_buf.append('string ')
    string = ''.join(string_buf)
    end = time()
    return end - start

def merge_using_list_operation():
    string = ''
    start = time()
    string_buf = []
    for _i in range(100000):
        string_buf += ['string ']
    string = ''.join(string_buf)
    end = time()
    return end - start

if __name__ == '__main__':
    print(f'merge_using_string_operation: {merge_using_string_operation()}')
    print(f'merge_using_list_append:      {merge_using_list_append()}')
    print(f'merge_using_list_operation:   {merge_using_list_operation()}')