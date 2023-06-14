#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer to the linked list to check.
 * Returns: 1 if palindrome or 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head, *tmp = *head;
	int count = 0, half, i = 0, second_half, n = 0, tester = 0;

	if (*head == NULL)
		return (1);

	while (current != NULL)
	{
		count++;
		current = current->next;
	}

	half = (count / 2) - 1;
	second_half = count / 2;
	while (half >= 0)
	{
		current = *head;
		i = 0;
		while (current != NULL && i < half)
		{
			current = current->next;
			i++;
		}
		if (current != NULL)
		{
			while (tmp != NULL)
			{
				if (n == second_half)
					if (current->n == tmp->n)
					{
						second_half++;
						tester++;
						tmp = *head;
						break;
					}
				n++;
				tmp = tmp->next;
			}
			n = 0;
		}
		half--;
	}
	if (tester == count / 2)
		return (1);
	else
		return (0);
}
