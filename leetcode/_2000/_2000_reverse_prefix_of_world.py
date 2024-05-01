class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        
        ch_index = word.index(ch)
        prefix_str = word[:ch_index + 1]
        remianing_str = word[ch_index + 1:]
        
        def reverse(s: str) -> str:
            string = [s[i] for i in range(len(s) -1, -1, -1)]
            return "".join(string)

        return reverse(prefix_str) + remianing_str
        

   
if __name__ == "__main__":
    print(Solution().reversePrefix("abcdefd", "d"))
