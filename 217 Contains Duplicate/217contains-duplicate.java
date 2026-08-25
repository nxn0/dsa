class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> sNos = new HashSet<>();
        for (int num : nums){
            if (sNos.contains(num)){
                return true;
            }
            sNos.add(num);
        }
        return false;
    }
}