#include "binary_trees.h"
#include "14-binary_tree_balance.c"

/**
 *binary_tree_is_perfect - checks if tree is perfect
 *@tree: a pointer to the node to find the sibling
 *Return: return 0 if null
 */

int binary_tree_is_perfect(const binary_tree_t *tree)
{
	if (!tree || binary_tree_balance(tree) != 0)
		return (0);
	if (!tree->left && !tree->right)
		return (1);
	if ((tree->left) && (tree->right))
		return (binary_tree_is_perfect(tree->left)
				&& binary_tree_is_perfect(tree->right));
	return (0);
}
