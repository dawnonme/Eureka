#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

class Queen {
private:
    int size;
    char** maze;
    int** attackmatrix;
public:
    Queen(int n);
    ~Queen();

    void showQueen() const;
    void getAttackMatrix();
    int countAttack() const;
    int getQueenAt(int col) const;
    void swap(char& a, char& b);
    void moveQueen();
    void showAtt() const;
};

Queen::Queen(int n) {
    size = n;
    maze = new char* [size];
    attackmatrix = new int* [size];
    for (int i = 0; i < size; ++i) {
        maze[i] = new char [size];
        attackmatrix[i] = new int [size];
    }
    for (int i = 0 ; i < size; ++i) {
        for (int j = 0; j < size; ++j) {
            if (i == 0) {
                maze[i][j]='Q';
            } 
            else {
                maze[i][j]='-';
            }
            attackmatrix[i][j] = 0;
        }
    }
}

Queen::~Queen() {
    for (int i = 0; i < size; ++i) {
        delete [] maze[i];
        delete [] attackmatrix[i];
    }
    delete [] maze;
    delete [] attackmatrix;
}

void Queen::showQueen() const {
    for (int i=0;i<size;++i) {
        for (int j=0;j<size;++j) {
            cout << maze[i][j] << " ";
        } 
        cout << endl;
    }
}

int Queen::getQueenAt(int col) const {
    for (int i=0;i<size;i++) {
        if (maze[i][col]=='Q')
            return i;
    }
    return 0;
}

int Queen::countAttack() const {
    int att=0;
    for (int i=0;i<size-1;i++) {
        for (int j=i+1;j<size;j++) {
            if (this->getQueenAt(i)==this->getQueenAt(j))
                att++;
            else if (abs(this->getQueenAt(i)-this->getQueenAt(j))==j-i)
                att++;
        }
    }
    return att;
}

void Queen::getAttackMatrix() {
    attackmatrix = new int* [size];
    for (int i=0;i<size;++i) {
        attackmatrix[i] = new int [size];
    }
    for (int i=0;i<size;++i) {
        for (int j=0;j<size;++j) {
            if (maze[i][j]=='Q') {
                attackmatrix[i][j]=this->countAttack();
            }
            else {
                int currentPos=this->getQueenAt(j);
                this->swap(maze[i][j],maze[currentPos][j]);
                attackmatrix[i][j]=this->countAttack();
                this->swap(maze[i][j],maze[currentPos][j]);         
            }
        }
    }
}

void Queen::swap(char& a,char& b) {
    char temp = a;
    a = b;
    b = temp;
}

void Queen::moveQueen() {
    this->getAttackMatrix();
    int I=0,J=0;
    for (int i=0;i<size;++i) {
        for (int j=0;j<size;++j) {
            if (attackmatrix[i][j]>=0) {
                if (attackmatrix[i][j]<attackmatrix[I][J]) {
                    I = i;
                    J = j;
                }
            }
        }
    }
    int location = this->getQueenAt(J);
    this->swap(maze[I][J],maze[location][J]);
}

void Queen::showAtt() const {
    for (int i=0;i<size;++i) {
        for (int j=0;j<size;++j) {
            cout << attackmatrix[i][j] << ' '; 
        }
        cout << endl;
    }
}

int main() {
    long double start = clock(),end;
    int size,counter=0;
    cin>>size;
    Queen queen(size);
    while (queen.countAttack()>0) {
        queen.moveQueen();
        ++counter;
        if (counter==100) {
            queen.showQueen();
            cout << "Attack: " << queen.countAttack() << endl;
            end = clock();
            cout << "Time: " << (end-start) / 1000 << "s" << endl;
            return 0;
        }
    }
    queen.showQueen();
    cout << "Attack: " << queen.countAttack() << endl;
    end = clock();
    cout << "Time: " << (end-start) / 1000 << "s" << endl;
    return 0;
}

/*This is my first finished class!!!!!!!*/