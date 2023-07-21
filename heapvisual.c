#include "heapvisual.h"
#include "mm.h"

/* 
  log 每行有一个标识号前缀
    0 trace file name, heap start address
    + occupy
    - remove / realloc handling
    1 end
*/
void log_trace_init(FILE* fp, char *file_name, void *heap_start) {
  fprintf(fp, "0 %s %p\n", file_name, heap_start);
}

void log_trace_end(FILE* fp) {
  fprintf(fp, "1 1 1\n");
}

/* 
  下面的函数实现需要自行结合 mm.c 的实现，
  一般是利用内存中尚未被清空的 block size 来获取 old_size
*/
#define GET(p)		(*(unsigned int *)(p))
#define GET_SIZE(p)		(GET(p) & ~0x7)
#define HDRP(bp)	((char* )(bp) - 4)

void log_malloc(FILE* fp, void *p) {
  size_t size = GET_SIZE(HDRP(p));
  fprintf(fp, "+ %p %d\n", p, size);
}

static size_t old_size;

void log_realloc_1(FILE* fp, void *old_p) {
  old_size = GET_SIZE(HDRP(old_p));
}
void log_realloc_2(FILE* fp, void *old_p, void *new_p) {
  size_t new_size = GET_SIZE(HDRP(new_p));
  fprintf(fp, "- %p %d\n", old_p, old_size);
  fprintf(fp, "+ %p %d\n", new_p, new_size);
}

void log_free(FILE* fp, void *p) {
  size_t old_size = GET_SIZE(HDRP(p));
  fprintf(fp, "- %p %d\n", p, old_size);
}