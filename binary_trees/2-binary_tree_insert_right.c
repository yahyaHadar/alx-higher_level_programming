#include "binary_trees.h"
#include <stdio.h>
#include <stdlib.h>

/**
 *binary_tree_insert_right - inserts a node as the right-child of another node
 *@parent: a pointer to the node to insert the right-child in
 *@value: the value to store in the new node
 *Return: return a pointer to the created node, or NULL on failure or if parent
 *is NULL
 */

binary_tree_t *binary_tree_insert_right(binary_tree_t *parent, int value)
{
binary_tree_t *new;

if (!parent)
return (NULL);
new = malloc(sizeof(struct binary_tree_s));
if (!new)
return (NULL);
new->parent = parent;
new->n = value;
new->left = NULL;
new->right = parent->right;
if (parent->right)
{
parent->right->parent = new;
}
parent->right = new;

return (new);
}
