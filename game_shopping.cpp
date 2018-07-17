//http://codeforces.com/contest/1009/problem/A?locale=en

#include <iostream>
using namespace std;

int solution(int money[], int games[], int game_count, int money_count){
  int purchase = 0, game_ref = 0, money_ref = 0;
  while(game_count != 0 && money_count != 0){
    if(money[money_ref] >= games[game_ref]) {
      purchase++;
      money_ref++;
      game_ref++;
      money_count--;
      game_count--;
    } else {
      game_ref++;
      game_count--;
    }
  }
  return purchase;
}

int main() {
  int game_count, money_count;
  cin >> game_count >> money_count;
  int games[game_count], money[money_count];
  for(int i = 0; i < game_count; i++){
    cin >> games[i];
  }
  for(int j = 0; j < money_count; j++){
    cin >> money[j]; 
  }
  cout << solution(money, games, game_count, money_count) << endl;

}
