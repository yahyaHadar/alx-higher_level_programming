#include "lists.h"

/**
 * check_cycle - checks if the linked list contains the cycle in it
 *
 * @list: the linked list that need to check
 *
 * Return: if list had a cycle is 1 if not it means 0
*/

int check_cycle(listint_t *list)
{
	listint_t *a = list;
	listint_t *b = list;

	if (!list)
		return (0);

	while (a && b && b->next)
	{
		a = a->next;
		b = b->next->next;
		if (a == b)
			return (1);
	}

	return (0);
}
