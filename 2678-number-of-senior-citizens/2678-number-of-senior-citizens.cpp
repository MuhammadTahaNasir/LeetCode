class Solution {
public:
    int countSeniors(const vector<string>& details) {
        int seniorCount = 0;

        for (const string& passengerInfo : details) {
            // Extract age directly from the substring and convert to integer
            int age = stoi(passengerInfo.substr(11, 2));

            // Check if the passenger is a senior (strictly over 60 years old)
            if (age > 60) {
                seniorCount++;
            }
        }

        return seniorCount;
    }
};