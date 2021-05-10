ENUM_OBJS = main.o enumeration.o


CXX = g++
#CXXFLAGS = -std=c++0x -c -g -O2 -Wall
CXXFLAGS = -std=c++0x -c -g -Wall
LD = g++
LDFLAGS = -std=c++0x -g -O2


all: enumeration

enumeration: $(ENUM_OBJS)
	$(LD) $(ENUM_OBJS) $(LDFLAGS) -o enumeration

main.o: main.cpp
	$(CXX) $(CXXFLAGS) main.cpp

enumeration.o: enumeration.cpp
	$(CXX) $(CXXFLAGS) enumeration.cpp

clean:
	-rm -f *.o enumeration


