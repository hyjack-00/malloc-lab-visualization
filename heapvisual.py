import cv2
import numpy as np
import os

heap_log_file = 'heap.log'
heap_visual_dir = 'heapvisual'

def visualize_heap_log(operations, max_heap_size, trace_file):
    width = 1920
    height = 1080

    # scale heap to 1920
    if max_heap_size > width:
        addr_scale_factor = width / max_heap_size
    else:
        addr_scale_factor = 1

    # scale ops rows to > 1080
    ops = len(operations)
    if ops > height:
        op_rows = 1
        height = ops
    else:
        op_rows = int(height / ops)

    # Space that hasn't been extended is marked gray
    heap_state = np.empty(width, dtype=np.uint8)
    heap_state.fill(64)

    image = np.zeros((height, width), dtype=np.uint8)
    
    # Draw by operations
    heap_used = 0
    for i, (op, addr, size, heap_size) in enumerate(operations):
        idx_start = int(addr * addr_scale_factor)
        idx_end = int((addr + size) * addr_scale_factor)
        idx_heap_size = int(heap_size * addr_scale_factor)

        heap_state[heap_used : idx_heap_size] = 0  # Extend heap
        heap_used = idx_heap_size

        if op == '+':
            heap_state[idx_start : idx_end] = 255  # Allocated: white
        elif op == '-':
            heap_state[idx_start : idx_end] = 0    # Free: black

        for r in range(i*op_rows, (i+1)*op_rows):
            image[r] = heap_state

    # Output image
    output_path = os.path.join('heapvisual', f'heap-{trace_file}.png')
    cv2.imwrite(output_path, image)
    print(f"Written to '{output_path}'")


def read_heap_log(filename):
    print("Log file:", filename)

    operations = []
    max_heap_size = 0
    heap_start_addr = 0
    trace_file = None

    with open(filename, 'r') as file:
        for line in file:
            tokens = line.strip().split()
            if tokens[0] == '0':     
                # init
                trace_file = os.path.basename(tokens[1])
                print("Reading trace file:", trace_file)
                heap_start_addr = int(tokens[2], 16)
            elif tokens[0] == '+':   
                # alloc
                addr = int(tokens[1], 16) - heap_start_addr
                size = int(tokens[2])
                heap_size = int(tokens[3])
                operations.append(('+', addr, size, heap_size))
            elif tokens[0] == '-':   
                # free
                addr = int(tokens[1], 16) - heap_start_addr
                size = int(tokens[2])
                heap_size = int(tokens[3])
                operations.append(('-', addr, size, heap_size))
            elif tokens[0] == '1':   # end
                max_heap_size = operations[-1][3]
                visualize_heap_log(operations, max_heap_size, trace_file)
                operations = []
                max_heap_size = 0
                heap_start_addr = 0


if __name__ == '__main__':
    if not os.path.exists(heap_visual_dir):
        os.makedirs(heap_visual_dir)

    read_heap_log(heap_log_file)