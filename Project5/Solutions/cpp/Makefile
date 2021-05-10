MDP_OBJS = main_mdp.o mdp.o
DTREE_OBJS = main_dtree.o dtree.o

MDP_SRC = main_mdp.cpp mdp.cpp
DTREE_SRC = main_dtree.cpp dtree.cpp

CXX = g++
CXXFLAGS = -std=c++0x -c -g -Wall
LD = g++
LDFLAGS = -std=c++0x -g


all: mdp dtree

mdp: $(MDP_SRC)
	$(LD) $(MDP_SRC) $(LDFLAGS) -o mdp

dtree: $(DTREE_SRC)
	$(LD) $(DTREE_SRC) $(LDFLAGS) -o dtree

clean:
	-rm -f *.o mdp dtree


