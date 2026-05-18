class Solution {
    public String getFrequency(String s) {
        int[] charS = new int[26];

        for(char c : s.toCharArray()) {
            charS[c - 'a']++;
        }

        StringBuilder s1 = new StringBuilder();

        for(int i = 0; i < charS.length; i++) {
            if(charS[i] != 0) {
                s1.append((char)i + 'a').append(charS[i]);
            }
        }

        return s1.toString();
    }

    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap<>();

        if(strs.length > 0) {
            for(String str : strs) {
                String sortedString = getFrequency(str);

                if(!map.containsKey(sortedString)) {
                    map.put(sortedString, new ArrayList<>());
                }
                map.get(sortedString).add(str);
            }
        }

        List<List<String>> anag = new ArrayList<>(map.values());
        return anag;
    }
}
