//http://codeforces.com/contest/1009/problem/B?locale=en

#include <iostream>
#include <string>
using namespace std;

int main()
{
    string s, ans, ones;
    int counter, position = 0;
    cin >> s;
    
    
    for(auto c: s){
        if(c == '1'){
           counter++; 
        } else{
            ans+=c;
        }
    }
    
    while(position < ans.size() && ans[position] == '0'){
        position++;
    }
    
    ans.insert(position, string(counter, '1'));
    cout<<ans<<endl;

    return 0;
}
