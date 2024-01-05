#include "binary_trees.h"
#include <stddef.h>

/**
 *binary_tree_height - give the height of the tree
 *@tree : is a pointer to the root node of the tree to measure the height.
 *Return: 0 if null.
 */

size_t binary_tree_height(const binary_tree_t *tree)
{
	if (!tree || (!(tree->left) && !(tree->right)))
		return (0);

	if (binary_tree_height(tree->left) > binary_tree_height(tree->right))
		return (binary_tree_height(tree->left) + 1);
	else
		return (binary_tree_height(tree->right) + 1);
}
