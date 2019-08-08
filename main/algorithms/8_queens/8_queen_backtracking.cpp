#include <iostream>
#include <deque>
#include <ctime>
using namespace std;

static int counter = 0;

class Queen {
	typedef deque<string> strdeque;
	typedef deque<Queen> sList;

private:
	int m_size;
	strdeque queen;
	int rank;

public:
	Queen(int size);
	Queen(const Queen& q);
	~Queen() {}

	void printQueen() const;
	bool indexValid(int row, int col) const;
	bool isValid() const;
	void setQueen(int row);
	
    friend void getChildren(sList& frontier);
    friend bool isSolution(const Queen& q);
};

typedef deque<Queen> sList;

Queen::Queen(int size) : m_size(size), rank(0) {
	for (int i = 0; i < m_size; ++i) {
		string str(m_size, '-');
		queen.push_front(str);
	}
}

Queen::Queen(const Queen& q) {
	m_size = q.m_size;
	rank = q.rank;
	for (int i = 0; i < m_size; ++i) {
		string str = q.queen[i];
		queen.push_front(str);
	}
}

void Queen::printQueen() const {
	for (int i = 0; i < m_size; ++i) {
		for (int j = 0; j < m_size; ++j) {
			cout << queen[i][j] << "  ";
		}
		cout << endl;
	}
	cout << endl;
}

bool Queen::indexValid(int row, int col) const {
	if (row >= 0 && row < m_size && col >= 0 && col < m_size) {
		return true;
	}
	return false;
}

bool Queen::isValid() const {
	for (int i = 0; i < m_size; ++i) {
		for (int j = 0; j < m_size; ++j) {
			if (queen[i][j] == 'Q') {
				for (int l = 0; l < m_size; ++l) {
					if (l != i && queen[l][j] == 'Q') {
						return false;
					}
					if (l != j && queen[i][l] == 'Q'){
						return false;
					}
				}
				for (int k = 1 - m_size; k < m_size; ++k) {
					if (indexValid(i + k, j + k) && k != 0) {
						if (queen[i + k][j + k] == 'Q') {
							return false;
						}
					}
					if (indexValid(i + k, j - k) && k != 0) {
						if (queen[i + k][j - k] == 'Q') {
							return false;
						}
					}
				}
			}
		}
	}
	return true;
}

void Queen::setQueen(int row) {
	queen[row][rank] = 'Q';
	++rank;
}

void getChildren(sList& frontier) {
	if (!isSolution(frontier[0]) && !frontier[0].isValid()) {
		frontier.pop_front();
	} else if (!isSolution(frontier[0]) && frontier[0].isValid()){
		Queen temp = frontier[0];
		frontier.pop_front();
		sList tempList;
		for (int i = 0; i < temp.m_size; ++i) {
			Queen child(temp);
			child.setQueen(i);
			tempList.push_front(child);
		}
		for (int i = tempList.size() - 1; i >= 0; --i) {
			frontier.push_front(tempList[i]);
		}
	}
}

bool isSolution(const Queen& q) {
	if (q.rank == q.m_size && q.isValid()) {
		return true;
	}
	return false;
}

void printList(const sList& l) {
	for (unsigned int i = 0; i < l.size(); ++i) {
		l[i].printQueen();
	}
}

int main(int argc, char const *argv[]) {
	long double start = clock(), end = 0;
	sList frontier, solution;
	int size;
	cin >> size;
	Queen q(size);
	frontier.push_front(q);
	while (frontier.size() != 0) {
		if (isSolution(frontier[0])) {
			solution.push_front(frontier[0]);
			frontier.pop_front();
		} else {
			getChildren(frontier);
		}
	}
	if (solution.size() != 0) {
		for (unsigned int i = 0; i < solution.size(); ++i) {
			cout << "The " << counter << "th solution" << endl;
			solution[i].printQueen();
			++counter;
		}
	}
	end = clock();
	cout << "Time consuming: " << (end - start) / 1000 << 's' << endl;
	return 0;
}