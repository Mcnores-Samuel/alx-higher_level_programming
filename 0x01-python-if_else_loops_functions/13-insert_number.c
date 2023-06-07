#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer to the head node
 * @number: a number to assigh as value in the new node
 * Return: pointer to the location of the new node or NULL if fail
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *tmp_node, *current = *head;

	new_node = (listint_t *)malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}

	if ((*head)->n > number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	while (current->next != NULL)
	{
		tmp_node = current->next;
		if (current->n <= number && tmp_node->n > number)
		{
			current->next = new_node;
			new_node->next = tmp_node;
			return (new_node);
		}
		current = current->next;
	}

	current->next = new_node;
	return (new_node);
}
