#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

struct TreeNode
{
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

bool dfs_hasPathSum_helper(struct TreeNode *root, int targetSum, int prev_sum)
{
    int currSum;

    if (!root)
        return (false);

    currSum = prev_sum + root->val;

    if (currSum == targetSum && !(root->right || root->left))
        return (true);

    return ((dfs_hasPathSum_helper(root->right, targetSum, currSum) || dfs_hasPathSum_helper(root->left, targetSum, currSum)));

    return (false);
}
bool hasPathSum(struct TreeNode *root, int targetSum)
{

    if (!root)
        return (false);
    return dfs_hasPathSum_helper(root, targetSum, 0);
}
