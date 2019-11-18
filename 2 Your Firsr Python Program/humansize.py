SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

'''
Convert a file size to human‐readable form.
arguments:
    size ‐‐ file size in bytes
    a_kilobyte_is_1024_bytes ‐‐ if True (default), use multiples of 1024 if False, use multiples of 1000
Returns: string
'''
def approximate_size(size, a_kilobyte_is_1024_bytes=True):
    if size < 0:
        raise ValueError('number must be non‐negative') # 使用raise触发错误和异常: https://www.runoob.com/python3/python3-errors-execptions.html
    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000 # 
    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if  size < multiple:
            return '{0:.1f} {1}'.format(size, suffix) # "format" usage: https://www.runoob.com/python/att-string-format.html
    raise ValueError('number too large')

if __name__ == '__main__':
    print(approximate_size(1000000000000, False))
    print(approximate_size(1000000000000))
    print(approximate_size(-100))