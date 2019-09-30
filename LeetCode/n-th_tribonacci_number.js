/**
 * @param {number} n
 * @return {number}
 */




// 0 1 1 2 3 5 8 

memo = {}
memo[0] = 0
memo[1] = 1
memo[2] = 1

var tribonacci = function(n) {
    if(n in memo){
        return memo[n]
    }
    
    memo[n] = tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3); 
    return memo[n];
};
