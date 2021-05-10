
TIC_TAC_TOE_OBJS = main_tac_toe.o tic_tac_toe.o
SUDOKU_OBJS = main_sudoku.o sudoku.o


CXX = g++
CXXFLAGS = -std=c++0x -c -g -O2 -Wall
LD = g++
LDFLAGS = -std=c++0x -g -O2


all: tic_tac_toe sudoku

tic_tac_toe: $(TIC_TAC_TOE_OBJS)
	$(LD) $(TIC_TAC_TOE_OBJS) $(LDFLAGS) -o tic_tac_toe

sudoku: $(SUDOKU_OBJS)
	$(LD) $(SUDOKU_OBJS) $(LDFLAGS) -o sudoku

main_tac_toe.o: main_tac_toe.cpp
	$(CXX) $(CXXFLAGS) main_tac_toe.cpp

tic_tac_toe.o: tic_tac_toe.cpp
	$(CXX) $(CXXFLAGS) tic_tac_toe.cpp

main_sudoku.o: main_sudoku.cpp
	$(CXX) $(CXXFLAGS) main_sudoku.cpp

sudoku.o: sudoku.cpp
	$(CXX) $(CXXFLAGS) sudoku.cpp

clean:
	-rm -f *.o tic_tac_toe sudoku


