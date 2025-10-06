import sys

def solve():
    try:
        data = sys.stdin.read().splitlines()
    except:
        data = []

    if not data:
        return

    n = int(data[0])
    m = int(data[1])
    
    input_signals = {}
    
    current_line = 2
    for _ in range(n):
        name, signal = data[current_line].split()
        binary_signal = signal.replace('_', '0').replace('-', '1')
        input_signals[name] = binary_signal
        current_line += 1
        
    output_definitions = []
    for _ in range(m):
        output_definitions.append(data[current_line].split())
        current_line += 1
        
    signal_length = len(list(input_signals.values())[0])

    def op_and(a, b): return '1' if a == '1' and b == '1' else '0'
    def op_or(a, b): return '1' if a == '1' or b == '1' else '0'
    def op_xor(a, b): return '1' if a != b else '0'
    def op_nand(a, b): return '0' if a == '1' and b == '1' else '1'
    def op_nor(a, b): return '0' if a == '1' or b == '1' else '1'
    def op_nxor(a, b): return '0' if a != b else '1'

    gate_functions = {
        "AND": op_and,
        "OR": op_or,
        "XOR": op_xor,
        "NAND": op_nand,
        "NOR": op_nor,
        "NXOR": op_nxor
    }

    final_results = []

    for out_name, gate_type, in1_name, in2_name in output_definitions:
        
        signal1 = input_signals[in1_name]
        signal2 = input_signals[in2_name]
        op = gate_functions[gate_type]
        
        output_binary = ""
        for i in range(signal_length):
            bit1 = signal1[i]
            bit2 = signal2[i]
            output_binary += op(bit1, bit2)
            
        output_signal = output_binary.replace('0', '_').replace('1', '-')
        
        final_results.append(f"{out_name} {output_signal}")

    print('\n'.join(final_results))

solve()