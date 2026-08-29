class Solution {
    public int longestConsecutive(int[] nums) {
        if(nums.length==0)return 0;
        HashSet<Integer> ns = new HashSet<>();

        for(int i = 0; i< nums.length; i++){
            ns.add(nums[i]);
        }
        int lcs = 1;
        for(int num:ns){
            if(ns.contains(num-1)){
                continue;
            }
            else{
                int curr = num;
                int currsb = 1;
                while(ns.contains(curr+1)){
                    curr++;
                    currsb++;
                }
                lcs = Math.max(lcs , currsb);
            }

        }
        return lcs;
    }
}