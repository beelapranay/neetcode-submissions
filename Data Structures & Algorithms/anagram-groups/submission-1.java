class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap<>();

        if(strs.length >= 0) {
            for(int i = 0; i < strs.length; i++) {
                char[] charArray  = strs[i].toCharArray();
                Arrays.sort(charArray);
                String sortedString = new String(charArray);
                
                if(!map.containsKey(sortedString)) {
                    map.put(sortedString, new ArrayList<>());
                }
                map.get(sortedString).add(strs[i]);

            }
        }

        List<List<String>> anag = new ArrayList<>(map.values());
        return anag;
    }
}
