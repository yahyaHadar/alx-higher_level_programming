#include "binary_trees.h"
#include <stdio.h>
#include <stdlib.h>

/**
 *binary_tree_node - function that creates a binary tree node
 *@parent: the value to put in the new node
 *@value: the value to put in the new node
 *Return: return a pointer to the new node, or NULL on failure
 */

binary_tree_t *binary_tree_node(binary_tree_t *parent, int value)
{
	binary_tree_t *new_node;

	new_node = malloc(sizeof(struct binary_tree_s));
	if (!new_node)
		return (NULL);
	new_node->parent = parent;
	new_node->left = NULL;
	new_node->right = NULL;
	new_node->n = value;
	return (new_node);
}
