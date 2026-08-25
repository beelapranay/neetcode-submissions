class Solution {

    public String encode(List<String> strs) {
        String strE = "";
        for(String str : strs) {
            strE = strE + str + " ";
        }
        return strE;
    }

    public List<String> decode(String str) {
        List<String> finalList = new ArrayList<>(Arrays.asList(str.split(" ")));
        return finalList;
    }
}
