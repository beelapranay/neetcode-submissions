class Solution {

    public String encode(List<String> strs) {
        String strE = "";
        for(String str : strs) {
            strE += str.length() + "#" + str;
        }
        return strE;
    }

    public List<String> decode(String str) {
        List<String> finalList = new ArrayList<String>();

        int i  = 0;
        while(i < str.length()) {
            int j = str.indexOf("#", i);
            int length = Integer.parseInt(str.substring(i, j));
            finalList.add(str.substring(j + 1, j + 1 + length));
            i = j + 1 +length;
        }

        return finalList;
    }
}