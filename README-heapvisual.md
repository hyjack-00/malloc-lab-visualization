# Malloc Lab - Heap Visualization

## Modification

- add code in `mdriver.c` to log heap status 
- `heapvisual.c` `heapvisual.h`
  - Definition of new functions used in `mdriver.c`
- `heapvisual.py`
  - python script to generate image from heap log, using opencv 2

## Usage

### Requirement

python lib: 

- cv2
- numpy

### Visualization

- After running `mdriver`, heap log files will be generated. Running the `heapvisual.py` script will generate a visualization of the heap state for each trace file, in the specified folder.
  - Colors 
    - white: Allocated
    - Black: Free
    - Gray:  Unextended
  - The visualization results will faithfully reflect the output of your memory allocator, and they will be influenced by the allocation algorithm and data structures used.
- Note that the implementation of `log_malloc`, `log_free`, and `log_realloc` in `heapvisual.c` depends on your own implementation in `mm.c`. Depending on the implementation of `mm_[]` functions, you may need to modify them.
  - By default, it uses the block header structure provided in the CSAPP source code.
- Configurable Settings
  - The default log file is named `heap.log`, which can be changed in both `mdriver.c` and `heapvisual.py` by modifying the `heap_log_file` variable.
  - The default folder for generated images is `heapvisual`, which can be modified in `heapvisual.py` by changing the `heap_visual_dir` variable.
  - In `heapvisual.py`, the width of the generated images (`width`) is fixed at 1920 pixels, and the height (`height`) is at least 1080 pixels, which could be up to the number of operations in the trace without upper limit.

### Turnoff

- If you want to maximize the execution speed of the program or revert back to the original CMU 15-213 source code version, simply comment out the `#define HEAP_VISU