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
		if (current_node->next == list && list != NULL)
			return (1);
		current_node = current_node->next;
	}
	return (0);
}
