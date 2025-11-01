import sys

def compress_ipv6(ip):
    blocks = ip.split(':')
    cleaned_blocks = []
    
    for block in blocks:
        if block == '0000':
            cleaned_blocks.append('0')
        else:
            cleaned_blocks.append(block.lstrip('0'))
            
    max_len = 0
    max_start = -1
    current_len = 0
    current_start = -1
    
    for i, block in enumerate(cleaned_blocks):
        if block == '0':
            if current_len == 0:
                current_start = i
            current_len += 1
        else:
            if current_len > max_len and current_len >= 2:
                max_len = current_len
                max_start = current_start
            current_len = 0
            current_start = -1

    if current_len > max_len and current_len >= 2:
        max_len = current_len
        max_start = current_start
        
    if max_len >= 2:
        result_blocks = cleaned_blocks[:max_start] + [''] + cleaned_blocks[max_start + max_len:]
        output = ':'.join(result_blocks)
        output = output.replace(':::', '::')
        
        if output.startswith(':'):
            output = ':' + output
        if output.endswith(':'):
            output = output + ':'
            
        output = output.replace(':::', '::')
    else:
        output = ':'.join(cleaned_blocks)
        
    return output

if __name__ == "__main__":
    ip = sys.stdin.read().strip()
    if ip:
        print(compress_ipv6(ip))