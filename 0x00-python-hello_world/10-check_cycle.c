#include "lists.h"
/**
*check_cycle - checks if there is a loop in a linked list
*@list: head of a linked list
*Return: 0 if no loop and 1 if loop is present
*/
int check_cycle(listint_t *list)
{
	listint_t *hare;
	listint_t *tortoise;

	if (list == NULL || list->next ==  NULL)
	{
		return (0);
	}
	hare = NULL;
	tortoise = NULL;
	hare = list;
	tortoise = list;
	while (hare != NULL && hare->next != NULL)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;
		if (tortoise == hare)
		{
			return (1);
		}
	}
	return (0);
}
