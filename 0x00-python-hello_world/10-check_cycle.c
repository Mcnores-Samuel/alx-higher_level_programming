#include "lists.h"

/**
 * check_cycle - checks if and linke list is circular or not.
 * @list: point to the head node of the list
 * Return: 0 if not a circular list or 1 if circular
 */
int check_cycle(listint_t *list)
{
	listint_t *current_node;

	if (list == NULL || list->next == NULL)
		return (0);

	current_node = list->next;

	while (current_node != NULL && current_node->next != NULL)
	{
		if (current_node == list)
			return (1);
		list = list->next;
		current_node = current_node->next->next;
	}
	return (0);
}
