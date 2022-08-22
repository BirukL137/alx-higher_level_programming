#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly linked list.
 *
 * Return: If there is no cycle - 0. If there is a cycle - 1.
 */

int check_cycle(listint_t *list)
{
	listint_t *turtle, *mule;

	if (list == NULL || list->next == NULL)
		return (0);

	turtle = list->next;
	mule = list->next->next;

	while (turtle && mule && mule->next)
	{
		if (turtle == mule)
			return (1);

		turtle = turtle->next;
		mule = mule->next->next;
	}

	return (0);
}
