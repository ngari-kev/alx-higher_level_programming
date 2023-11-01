#include "lists.h"

/**
 * insert_node - inserts a node into a sorted linked list
 * @head: pointer to the start of a linked list
 * @number: the value to add to the new node
 * Return: pointer to new node or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode, *current, *previous;

	current = *head;
	previous = NULL;
	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);
	newnode->n = number;
	newnode->next = NULL;
	if (*head == NULL || number < (*head)->n)
	{
		newnode->next = *head;
		*head = newnode;
		return (newnode);
	}

	while (current != NULL && current->n < number)
	{
		previous = current;
		current = current->next;
	}
	previous->next = newnode;
	newnode->next = current;
	return (newnode);
}

