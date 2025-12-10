class Solution {
public:
    int compress(vector<char>& chars) {
        int writeIndex = 0; // Index to write the compressed result
        int readIndex = 0;  // Index to read characters from the input
        int n = chars.size(); // Size of the input vector
        
        while (readIndex < n) {
            char currentChar = chars[readIndex];
            int count = 0;
            
            // Count occurrences of the current character
            while (readIndex < n && chars[readIndex] == currentChar) {
                readIndex++;
                count++;
            }
            
            // Write the character to the result
            chars[writeIndex++] = currentChar;
            
            // Write the count if it's more than 1
            if (count > 1) {
                for (char c : to_string(count)) {
                    chars[writeIndex++] = c;
                }
            }
        }
        
        return writeIndex; // The new length of the compressed vector
    }
};
