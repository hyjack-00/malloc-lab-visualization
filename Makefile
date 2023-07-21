CC = gcc
CFLAGS = -Wall -O2 -m32 -Wno-unused-result -Wno-unused-function
CFLAGS_DEBUG = -Wall -O0 -g -m32 -Wno-unused-result -Wno-unused-function

OBJS = mdriver.o mm.o memlib.o fsecs.o fcyc.o clock.o ftimer.o heapvisual.o

mdriver: $(OBJS)
	$(CC) $(CFLAGS) -o mdriver $(OBJS)

mdriver_debug: $(OBJS)
	$(CC) $(CFLAGS_DEBUG) -o mdriver_debug $(OBJS)

mdriver.o: mdriver.c fsecs.h fcyc.h clock.h memlib.h config.h mm.h
memlib.o: memlib.c memlib.h
mm.o: mm.c mm.h memlib.h
fsecs.o: fsecs.c fsecs.h config.h
fcyc.o: fcyc.c fcyc.h
ftimer.o: ftimer.c ftimer.h config.h
clock.o: clock.c clock.h
heaplog.o: heaplog.c heaplog.h

clean:
	rm -f *~ *.o mdriver mdriver_debug

debug: clean
	$(MAKE) CFLAGS="$(CFLAGS_DEBUG)" mdriver_debug
	gdb mdriver_debug -x gdbinit
