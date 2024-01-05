#include "binary_trees.h"
#include <stdlib.h>

/**
 *binary_tree_rotate_left - performs a left-rotation on a binary tree
 *@tree: A pointer to the root node of the tree to rotate.
 *Return: A pointer to the new root node after rotation.
 */
binary_tree_t *binary_tree_rotate_left(binary_tree_t *tree)
{
	binary_tree_t *p, *tmp;

	if (tree == NULL || tree->right == NULL)
		return (NULL);
	p = tree->right;
	tmp = p->left;
	p->left = tree;
	tree->right = tmp;
	if (tmp != NULL)
		tmp->parent = tree;
	tmp = tree->parent;
	tree->parent = p;
	p->parent = tmp;
	if (tmp != NULL)
	{
		if (tmp->left == tree)
			tmp->left = p;
		else
			tmp->right = p;
	}
	return (p);
}
