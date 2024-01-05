#include "binary_trees.h"
#include <stddef.h>

/**
 *binary_tree_depth - give the depth of the tree
 *@tree : is a pointer to the root node of the tree to measure the depth.
 *Return: 0 if null.
 */

size_t binary_tree_depth(const binary_tree_t *tree)
{
	if (!tree || !(tree->parent))
		return (0);
	return (binary_tree_depth(tree->parent) + 1);
}
