class Solution {
public:
    bool isPalindrome(int x) {
        
        int originalValue = x;
        long reverseValue = 0;
        while (x > 0){
            int lastDigit = x % 10; 
            x = (int) x/10;

            if(reverseValue * 10 <= INT_MIN) return 0;
            if(reverseValue * 10 >= INT_MAX) return 0;
            
            reverseValue = (reverseValue * 10) + lastDigit;
        }
        return reverseValue == originalValue;
    }
};