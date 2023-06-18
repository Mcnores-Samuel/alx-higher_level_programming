#include "lists.h"

/**
 * check_cycle - checks if and linke list is circular or not.
 * @list: point to the head node of the list
 * Return: 0 if not a circular list or 1 if circular
 */
int check_cycle(listint_t *list)
{
	listint_t *current_node;

	if (list == NULL)
		return (0);

	current_node = list;

	while (current_node != NULL)
	{
		if (current_node->next == list && list->n == current_node->n)
			break;
		current_node = current_node->next;
	}

	if (current_node == NULL)
		return (0);

	return (1);
}
