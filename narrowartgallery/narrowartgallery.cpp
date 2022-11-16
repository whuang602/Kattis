#include <iostream>
#include <algorithm>
#include <vector>



int closed_cost(int K, int N, int room_list[][2], std::vector<std::vector<std::vector<int>>>& dp_table, int row, int column); 

int main() {

int N, K;
std::cin >> N >> K;
int room_list[N][2];
int a,b;
for (int i = 0 ; i < N ; i++) {
    std::cin >> a >> b;
    room_list[i][0] = a;
    room_list[i][1] = b;
}
std::cin >> a >> b;

// int dp_table[K+1][N][2];
std::vector<std::vector<std::vector<int>>> dp_table;
dp_table = std::vector<std::vector<std::vector<int>>>(K+1, std::vector<std::vector<int>>(N, std::vector<int>(2,-1)));

int total = 0;
for (int i = 0 ; i < N ; i++)
 	total += room_list[i][0] + room_list[i][1];

 std::cout << total - std::min(closed_cost(K,N, room_list, dp_table, 0,0), closed_cost(K, N, room_list, dp_table, 0,1));
	
}

int closed_cost(int K, int N, int room_list[][2], std::vector<std::vector<std::vector<int>>>& dp_table, int row, int column) {
    int flipper[2] = {1,0};
    if (K <= 0)
        return 0;
    
    if (row > N-1)
        return 40000;
    
    if (dp_table[K][row][column] < 0) {
        int block_next_room = room_list[row][column] + closed_cost(K-1,N, room_list, dp_table, row+1, column);
        return std::min(std::min(block_next_room, closed_cost(K,N, room_list, dp_table, row+1, column)), closed_cost(K, N, room_list, dp_table, row+1, flipper[column]));
    }
    return dp_table[K][row][column];
}