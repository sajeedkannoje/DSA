class Solution {
public:
    int reverse(int x) {

        long  rev = 0;
        while(true){
            if (x == 0) return rev;   
            int lastDigit = x % 10;
            x = (int) x/10;
            if ((rev * 10) <= INT_MIN ) return 0;
            if( (rev * 10) >= INT_MAX  ) return 0;
            rev = rev * 10 + lastDigit;
        }
    }
};