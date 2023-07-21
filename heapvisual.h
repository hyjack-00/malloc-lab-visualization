#include <stdio.h>

void log_trace_init(FILE* fp, char *file_name, void *mem_start);
void log_trace_end(FILE* fp);

void log_malloc(FILE* fp, void *addr);
void log_realloc_1(FILE* fp, void *old_p);
void log_realloc_2(FILE* fp, void *old_p, void *new_p);
void log_free(FILE* fp, void *p);