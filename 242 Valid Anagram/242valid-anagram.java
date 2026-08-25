class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }
        int[] charc = new int[26];
        for (int i=0; i< s.length(); i++){
                charc[s.charAt(i) - 'a']++;
                charc[t.charAt(i) - 'a']--;
        }
        for( int count: charc){
            if(count !=0){
                return false;
            }
        }
        return true;
    }
}