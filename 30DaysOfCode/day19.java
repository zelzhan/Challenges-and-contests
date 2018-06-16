import java.io.*;
import java.util.*;

interface AdvancedArithmetic{          //Interface which I had to implement
   int divisorSum(int n);
}

class Calculator implements AdvancedArithmetic{ //actual class
    public int divisorSum(int n){
        int counter = 0;
        for(int i = 1; i <= n; i++){
            if(n%i == 0) counter+=i;   //counter will sum up all multiples of number n
        }
        return counter;
    }
}

class Solution {            //tester

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        scan.close();
        
      	AdvancedArithmetic myCalculator = new Calculator(); 
        int sum = myCalculator.divisorSum(n);
        System.out.println("I implemented: " + myCalculator.getClass().getInterfaces()[0].getName() );
        System.out.println(sum);
    }
}
