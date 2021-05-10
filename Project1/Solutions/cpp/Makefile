
SRC := main.cpp mysearch.cpp $(wildcard helpers/*.cpp) 

ROUTE_SRC = ${SRC}
ROUTE_SRC += route.cpp

TSP_SRC = ${SRC}
TSP_SRC += tsp.cpp

CXX = g++
CXXFLAGS = -std=c++0x -c -g -O0 -Wall
LD = g++
LDFLAGS =  -std=c++0x -g -fpermissive

all: route tsp

route: $(ROUTE_SRC)
	$(LD) $(ROUTE_SRC) $(LDFLAGS) -DUSING_ROUTE -o route

tsp: $(TSP_SRC)
	$(LD) $(TSP_SRC) $(LDFLAGS) -o tsp

clean:
	-rm -f *.o route tsp




