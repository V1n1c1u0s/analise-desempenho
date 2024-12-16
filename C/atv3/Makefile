CC = g++
CCFLAGS = -O3 -march=native -flto -funroll-loops -fomit-frame-pointer -ffast-math -std=c++11 # Flags do compilador
EXEC_QUICK = quicksort
EXEC_BUBBLE = bubblesort
EXEC_MERGE = mergesort


all: $(EXEC_QUICK) $(EXEC_BUBBLE) $(EXEC_MERGE)

$(EXEC_QUICK): quicksort.cpp
	$(CC) $(CCFLAGS) quicksort.cpp -o $(EXEC_QUICK)

$(EXEC_BUBBLE): bubblesort.cpp
	$(CC) $(CCFLAGS) bubblesort.cpp -o $(EXEC_BUBBLE)

$(EXEC_MERGE): mergesort.cpp
	$(CC) $(CCFLAGS) mergesort.cpp -o $(EXEC_MERGE)

clean:
	rm -f $(EXEC_QUICK) $(EXEC_BUBBLE) $(EXEC_MERGE)

run: $(EXEC_QUICK) $(EXEC_BUBBLE) $(EXEC_MERGE)
	./$(EXEC_QUICK)
	./$(EXEC_BUBBLE)
	./$(EXEC_MERGE)

# garante que todos os arquivos sejam compilados antes
.PHONY: all clean run
