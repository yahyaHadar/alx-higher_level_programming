#include "binary_trees.h"
#include <stddef.h>

/**
 *binary_tree_size - give the size of the tree
 *@tree : is a pointer to the root node of the tree to measure the size.
 *Return: 0 if null.
 */

size_t binary_tree_size(const binary_tree_t *tree)
{
	if (!tree)
		return (0);
	return (binary_tree_size(tree->right) + binary_tree_size(tree->left) + 1);
}
