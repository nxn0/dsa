int lengthOfLongestSubstring(char* s) {
    int n = strlen(s);
    if(n==0) return 0;
    int las[128];
    for (int i = 0;i< 128; i++) las[i] = -1;
    int max = 0;
    int left = 0;
    for (int right = 0; right < n; right++){
        if (las[(int)s[right]] >= left){
            left = las[(int)s[right]] + 1;
        }
    las[(int)s[right]] = right;
    int crln = right - left + 1;
    if (crln > max)
    {
        max= crln;
    }
    }
    return max;
}