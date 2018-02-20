#include <iostream>
#include <vector>

using namespace std;

int row;
int col;
char mus[1001][1001];
int res[1001][1001];
int pics;

void recurseHelp(int x, int y) {
    if (x < 0 || x >= row || y < 0 || y >= col) {
        return;

    }
    if(res[x][y]){
        return;
    }
    if(mus[x][y] == '*'){
        pics ++;
        return;
    }
    res[x][y] = 1;
    recurseHelp(x + 1, y);
    recurseHelp(x, y - 1);
    recurseHelp(x - 1, y);
    recurseHelp(x, y + 1);
    res[x][y] = pics;
}

int main() {
    int picCount = 0;
    cin >> row;
    cin >> col;
    int loops = 0;
    cin >> loops;



}

