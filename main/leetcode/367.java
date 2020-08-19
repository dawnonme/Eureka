class Solution {
    public boolean isPerfectSquare(int num) {
        long lo = 1, hi = num;
        long mid = lo + (hi - lo) / 2;
        long s = mid * mid;
        Biginteger a = 10;
        while (s != num) {
            if (s > num) {
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
            if (lo > hi) {
                return false;
            }

            mid = lo + (hi - lo) / 2;
            s = mid * mid;
        }
        HashSet
        return true;
    }

    public Integer a() {
        i
    }

    public final int a;

}

public class sumn {

}

