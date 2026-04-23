

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* shuffle(int* nums, int numsSize, int n, int* returnSize){
    *returnSize=numsSize;
    int* res = (int*)malloc(numsSize*sizeof(int));
    int *t = res;
    int *xp = nums;
    int *yp = nums + n;

    for(int i=0;i<n;i++){
       *(t++)=*(xp++);
       *(t++)=*(yp++);
    }
    return res;
}