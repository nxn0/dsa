bool isMatch(char* s, char* p) {
    char *sptr = s, *pptr = p;
    char *stmp = NULL, *star = NULL;
    while(*sptr){
        if(*pptr == '?' || *pptr == *sptr){
            sptr++; pptr++;
        }
    else if(*pptr=='*'){
        star=pptr;
        stmp=sptr;
        pptr++;
        }
    else if(star){
        pptr=star+1;
        stmp++;
        sptr=stmp;
        }
    else return false;
    }
while(*pptr=='*')pptr++;
return !*pptr;
}