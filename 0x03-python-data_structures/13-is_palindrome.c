#include "lists.h"

/**
* is_palindrome - Checks if it is a palindrome
* @head: Pointer to a pointer
*
* Return: 0 if it is not a palindrome
*/
int is_palindrome(listint_t **head)
{
listint_t *current = *head;
int values[1024];
int i, j;

if (*head == NULL || (*head)->next == NULL)
return (1);

for (i = 0;  current != NULL;  i++)
{
values[i] = current->n;
current = current->next;
}

for (j = 0;  j < i / 2;  j++)
{
if (values[j] != values[i - j - 1])
return (0);
}

return (1);
}
