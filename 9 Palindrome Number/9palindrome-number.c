bool isPalindrome(int x) {
    if (x < 0) return 0;

    int o= x;
    int r= 0;

    while (x != 0){
        int d= x % 10;
        if (r> (INT_MAX - d) / 10){
            return false;
        }
        r = r * 10 + d;
        x = x / 10;
    }

    if (o == r ) return true;
    else return false;
}