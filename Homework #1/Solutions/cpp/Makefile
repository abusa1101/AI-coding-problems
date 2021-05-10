CXXFLAGS = -std=c++0x -g

all: cell quicksort mygraph

cell:
	g++ $(CXXFLAGS) cell.cpp -o cell

quicksort: 
	g++ $(CXXFLAGS) quicksort.cpp -o quicksort

mygraph:
	g++ $(CXXFLAGS) mygraph.cpp -o mygraph

clean:
	-rm -f *.o
	-rm -f cell quicksort mygraph
