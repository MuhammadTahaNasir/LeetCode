class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> result;
        vector<int> combination;
        sort(candidates.begin(), candidates.end());  // Sort candidates to handle duplicates and facilitate pruning.
        findCombinations(candidates, target, 0, combination, result);
        return result;
    }

private:
    void findCombinations(vector<int>& candidates, int target, int start,
                          vector<int>& combination, vector<vector<int>>& result) {
        if (target == 0) {
            result.push_back(combination);
            return;
        }

        for (int i = start; i < candidates.size(); ++i) {
            if (i > start && candidates[i] == candidates[i - 1]) continue;  // Skip duplicates

            if (candidates[i] > target) break;  // Prune the recursion tree, as further elements will also be too large.

            combination.push_back(candidates[i]);
            findCombinations(candidates, target - candidates[i], i + 1, combination, result);
            combination.pop_back();  // Backtrack
        }
    }
};
